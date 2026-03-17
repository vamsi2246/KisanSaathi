from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

class FarmInput(BaseModel):
    Soil_Type: str
    Farm_Area_acres: float
    Water_Availability_L_per_week: int
    Irrigation_Type: str
    Fertilizer_Used_kg: float
    Season: str
    Rainfall_mm: float
    Temperature_C: float
    Soil_pH: float

app = FastAPI(
    title="Farm Planner Backend",
    description="API for crop prediction and farm management",
    version="1.0.0"
)

allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from typing import List

class OptimizationInput(BaseModel):
    land_area: float
    water_available: float
    fertilizer_available: float
    candidate_crops: List[str]

class EnrichedOptimizationInput(FarmInput):
    land_area: float
    water_available: float
    fertilizer_available: float
    candidate_crops: List[str]

class FarmPlanInput(FarmInput):
    land_area: float
    water_available: float
    fertilizer_available: float

RELATED_CROPS = {
    "Rice":   ["Rice", "Wheat", "Maize"],
    "Wheat":  ["Wheat", "Potato", "Maize"],
    "Tomato": ["Tomato", "Potato", "Wheat"],
    "Maize":  ["Maize", "Rice", "Wheat"],
    "Potato": ["Potato", "Tomato", "Maize"],
}
DEFAULT_RELATED = ["Wheat", "Maize", "Potato"]

class YieldInput(FarmInput):
    crop_name: str
    acres: float

from services.prediction import predict_crop
from services.optimizer import optimize_allocation
from services.yield_predictor import predict_yield, calculate_profit
from services.preprocessor import safe_preprocess
from services.environment import analyze_environment, generate_advisories


def _sustainability_score(enriched: dict) -> int:
    """Compute a 0–100 sustainability score based on crop risk levels."""
    risk_scores = {"Low": 100, "Medium": 60, "High": 20}
    if not enriched:
        return 0
    total = sum(risk_scores.get(d["risk_level"], 20) for d in enriched.values())
    return round(total / len(enriched))


def enrich_allocation(allocation: dict, farm_conditions: dict) -> dict:
    """Enrich each allocated crop with yield, env analysis, advisories, and profit."""
    enriched = {}
    for crop_name, acres in allocation.items():
        if acres <= 0:
            continue

        base_yield = predict_yield(farm_conditions, crop_name=crop_name)
        env = analyze_environment(farm_conditions, crop_name=crop_name, predicted_yield=base_yield)
        adjusted_yield = env["adjusted_yield"]
        advisories = generate_advisories(farm_conditions, crop_name=crop_name)
        profit = calculate_profit(adjusted_yield, acres, crop_name)

        enriched[crop_name] = {
            "acres":          acres,
            "expected_yield": base_yield,
            "adjusted_yield": adjusted_yield,
            "expected_profit":profit,
            "risk_level":     env["risk_level"],
            "advisories":     advisories
        }
    return enriched

@app.get("/")
async def root():
    return {"message": "Farm Planner Backend Running"}

@app.post("/predict-crop")
async def predict_crop_endpoint(data: FarmInput):
    try:
        input_dict = safe_preprocess(data.model_dump())
        prediction = predict_crop(input_dict)
        return {"recommended_crop": prediction}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during prediction: {str(e)}"
        )

@app.post("/optimize-allocation")
async def optimize_allocation_endpoint(data: EnrichedOptimizationInput):
    try:
        farm_conditions = safe_preprocess(
            data.model_dump(
                exclude={"land_area", "water_available", "fertilizer_available", "candidate_crops"}
            )
        )

        result = optimize_allocation(
            land_area=data.land_area,
            water_available=data.water_available,
            fertilizer_available=data.fertilizer_available,
            crop_names=data.candidate_crops
        )

        enriched = enrich_allocation(result["allocation"], farm_conditions)

        return {
            "allocation": enriched,
            "resource_usage": result["resource_usage"],
            "total_profit": result["total_profit"]
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during optimization: {str(e)}"
        )


@app.post("/generate-farm-plan")
async def generate_farm_plan(data: FarmPlanInput):
    try:
        raw_input = data.model_dump(exclude={"land_area", "water_available", "fertilizer_available"})
        input_dict = safe_preprocess(raw_input)
        farm_conditions = input_dict
        predicted_crop = predict_crop(input_dict)

        candidate_crops = RELATED_CROPS.get(predicted_crop, DEFAULT_RELATED)

        optimization_result = optimize_allocation(
            land_area=data.land_area,
            water_available=data.water_available,
            fertilizer_available=data.fertilizer_available,
            crop_names=candidate_crops
        )

        enriched = enrich_allocation(optimization_result["allocation"], farm_conditions)

        farm_plan = [
            {
                "crop":           crop,
                "acres":          d["acres"],
                "expected_yield": d["expected_yield"],
                "adjusted_yield": d["adjusted_yield"],
                "expected_profit":d["expected_profit"],
                "risk_level":     d["risk_level"],
                "advisories":     d["advisories"]
            }
            for crop, d in enriched.items()
        ]
        total_expected_profit = round(
            sum(d["expected_profit"] for d in enriched.values()), 2
        )
        sustainability_score = _sustainability_score(enriched)

        return {
            "predicted_crop":       predicted_crop,
            "candidate_crops":      candidate_crops,
            "farm_plan":            farm_plan,
            "total_expected_profit":total_expected_profit,
            "sustainability_score": sustainability_score
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while generating the farm plan: {str(e)}"
        )


@app.post("/predict-yield")
async def predict_yield_endpoint(data: YieldInput):
    try:
        input_data = safe_preprocess(
            data.model_dump(exclude={"crop_name", "acres"})
        )

        yield_per_acre = predict_yield(input_data, crop_name=data.crop_name)

        total_production = round(yield_per_acre * data.acres, 3)
        profit = calculate_profit(
            yield_per_acre=yield_per_acre,
            acres=data.acres,
            crop_name=data.crop_name
        )

        return {
            "crop": data.crop_name,
            "acres": data.acres,
            "yield_per_acre": yield_per_acre,
            "total_production_tons": total_production,
            "profit": profit
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during yield prediction: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

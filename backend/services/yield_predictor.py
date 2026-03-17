import os
import joblib
import pandas as pd

BASE_DIR       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH     = os.path.join(BASE_DIR, "models", "yield_model.pkl")
ENCODERS_PATH  = os.path.join(BASE_DIR, "models", "yield_encoders.pkl")

try:
    _model    = joblib.load(MODEL_PATH)
    _encoders = joblib.load(ENCODERS_PATH)
except FileNotFoundError as e:
    raise FileNotFoundError(
        f"Yield model or encoders not found. "
        f"Please run train_yield_model.py first.\nError: {e}"
    )

FEATURE_COLUMNS = [
    "Soil_Type",
    "Farm_Area_acres",
    "Water_Availability_L_per_week",
    "Irrigation_Type",
    "Fertilizer_Used_kg",
    "Season",
    "Rainfall_mm",
    "Temperature_C",
    "Soil_pH",
    "Crop",
]

CATEGORICAL_COLUMNS = ["Soil_Type", "Irrigation_Type", "Season", "Crop"]

MARKET_PRICE = {
    "Tomato": 12000,
    "Wheat":   8000,
    "Rice":    9000,
    "Potato":  7000,
    "Maize":   6000,
}


def calculate_profit(yield_per_acre: float, acres: float, crop_name: str) -> float:
    """Calculate total profit from a crop harvest."""
    if crop_name not in MARKET_PRICE:
        raise ValueError(
            f"No market price found for '{crop_name}'. "
            f"Supported crops: {list(MARKET_PRICE.keys())}"
        )
    price_per_ton = MARKET_PRICE[crop_name]
    total_profit  = yield_per_acre * acres * price_per_ton
    return round(total_profit, 2)


def _encode_input(input_df: pd.DataFrame) -> pd.DataFrame:
    """Apply saved LabelEncoders to categorical columns."""
    for col in CATEGORICAL_COLUMNS:
        if col not in _encoders:
            continue
        le = _encoders[col]
        unseen = set(input_df[col].astype(str)) - set(le.classes_)
        if unseen:
            raise ValueError(
                f"Unknown value(s) {unseen} for column '{col}'. "
                f"Accepted values: {list(le.classes_)}"
            )
        input_df[col] = le.transform(input_df[col].astype(str))
    return input_df


def predict_yield(input_data: dict, crop_name: str) -> float:
    """Predict crop yield in tons per acre for given farm conditions."""
    data = {**input_data, "Crop": crop_name}
    row = pd.DataFrame([data])[FEATURE_COLUMNS]
    row = _encode_input(row)

    prediction = _model.predict(row)[0]
    return round(float(prediction), 3)

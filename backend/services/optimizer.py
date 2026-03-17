import pulp
from typing import Dict, Any, List

CROP_DATA = {
    "Rice": {
        "profit": 45000,
        "water": 4500,
        "fertilizer": 100
    },
    "Wheat": {
        "profit": 35000,
        "water": 2000,
        "fertilizer": 60
    },
    "Tomato": {
        "profit": 60000,
        "water": 3000,
        "fertilizer": 80
    },
    "Maize": {
        "profit": 30000,
        "water": 1800,
        "fertilizer": 50
    },
    "Potato": {
        "profit": 50000,
        "water": 2500,
        "fertilizer": 90
    }
}


def optimize_allocation(
    land_area: float, 
    water_available: float, 
    fertilizer_available: float, 
    crop_names: List[str]
) -> Dict[str, Any]:
    """Optimizes crop allocation to maximize profit under given constraints using PuLP."""
    
    unknown_crops = [name for name in crop_names if name not in CROP_DATA]
    if unknown_crops:
        raise ValueError(
            f"Unknown crop(s): {unknown_crops}. "
            f"Supported crops are: {list(CROP_DATA.keys())}"
        )
    
    if not crop_names:
        raise ValueError("No crops provided. Please supply at least one crop name.")
    
    valid_crops = list(crop_names)
    
    prob = pulp.LpProblem("Crop_Allocation_Optimization", pulp.LpMaximize)
    
    crop_vars = pulp.LpVariable.dicts(
        "Acres", 
        valid_crops, 
        lowBound=0, 
        cat='Continuous'
    )
    
    prob += pulp.lpSum([crop_vars[name] * CROP_DATA[name]['profit'] for name in valid_crops]), "Total_Profit"
    
    prob += pulp.lpSum([crop_vars[name] for name in valid_crops]) <= land_area, "Total_Land_Constraint"
    prob += pulp.lpSum([crop_vars[name] * CROP_DATA[name]['water'] for name in valid_crops]) <= water_available, "Total_Water_Constraint"
    prob += pulp.lpSum([crop_vars[name] * CROP_DATA[name]['fertilizer'] for name in valid_crops]) <= fertilizer_available, "Total_Fertilizer_Constraint"
    
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    status = pulp.LpStatus[prob.status]
    if status in ("Infeasible", "Undefined", "Not Solved"):
        raise ValueError(
            f"Optimization failed: {status}. "
            "Resources (land, water, or fertilizer) may be insufficient to allocate any crop."
        )
    
    allocation = {}
    total_water_used = 0.0
    total_fertilizer_used = 0.0
    
    for name in valid_crops:
        var = crop_vars[name]
        allocated_acres = round(var.varValue, 2) if var.varValue is not None else 0.0
        allocation[name] = allocated_acres
        total_water_used += allocated_acres * CROP_DATA[name]['water']
        total_fertilizer_used += allocated_acres * CROP_DATA[name]['fertilizer']
        
    total_profit = pulp.value(prob.objective) if pulp.value(prob.objective) is not None else 0.0
    
    return {
        "allocation": allocation,
        "resource_usage": {
            "water_used": round(total_water_used, 2),
            "fertilizer_used": round(total_fertilizer_used, 2)
        },
        "total_profit": round(total_profit, 2)
    }

from typing import Any

FEATURE_DEFAULTS: dict[str, Any] = {
    "Soil_Type":                     "Loamy",
    "Irrigation_Type":               "Sprinkler",
    "Season":                        "Kharif",
    "Crop":                          "Wheat",
    "Farm_Area_acres":               10.0,
    "Water_Availability_L_per_week": 2750,
    "Fertilizer_Used_kg":            110.0,
    "Rainfall_mm":                   850.0,
    "Temperature_C":                 27.0,
    "Soil_pH":                       7.0,
}


def safe_preprocess(input_data: dict) -> dict:
    """Fills missing or None values in input_data with FEATURE_DEFAULTS."""
    processed = {}

    all_keys = set(FEATURE_DEFAULTS.keys()) | set(input_data.keys())

    for key in all_keys:
        value = input_data.get(key)
        is_missing = value is None or str(value).strip() == ""

        if is_missing:
            default = FEATURE_DEFAULTS.get(key)
            processed[key] = default
        else:
            processed[key] = value

    return processed

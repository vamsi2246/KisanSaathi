from typing import Any

CROP_RANGES: dict[str, dict[str, tuple]] = {
    "Wheat": {
        "temperature": (10.1, 17.7, 37.5, 45.0),
        "rainfall":    (200.0, 468.5, 1211.0, 1499.6),
        "soil_ph":     (5.0, 5.9, 8.1, 9.0),
    },
    "Potato": {
        "temperature": (10.0, 17.4, 37.5, 45.0),
        "rainfall":    (200.8, 495.5, 1243.8, 1498.8),
        "soil_ph":     (5.0, 5.8, 8.2, 9.0),
    },
    "Maize": {
        "temperature": (10.0, 17.4, 37.7, 45.0),
        "rainfall":    (200.5, 470.6, 1228.8, 1499.8),
        "soil_ph":     (5.0, 5.8, 8.1, 9.0),
    },
    "Tomato": {
        "temperature": (10.0, 17.3, 37.3, 45.0),
        "rainfall":    (200.6, 481.9, 1232.3, 1499.7),
        "soil_ph":     (5.0, 5.9, 8.2, 9.0),
    },
    "Rice": {
        "temperature": (10.0, 17.4, 37.7, 45.0),
        "rainfall":    (200.7, 466.1, 1220.9, 1499.4),
        "soil_ph":     (5.0, 5.9, 8.2, 9.0),
    },
    "Onion": {
        "temperature": (32.9, 33.2, 34.6, 34.9),
        "rainfall":    (1048.1, 1056.8, 1101.4, 1110.1),
        "soil_ph":     (7.2, 7.2, 7.3, 7.3),
    },
    "Garlic": {
        "temperature": (31.2, 31.5, 32.9, 33.2),
        "rainfall":    (905.4, 914.1, 958.7, 967.4),
        "soil_ph":     (7.1, 7.1, 7.2, 7.3),
    },
    "Carrot": {
        "temperature": (37.2, 37.4, 38.9, 39.1),
        "rainfall":    (969.6, 978.3, 1022.9, 1031.6),
        "soil_ph":     (7.4, 7.5, 7.6, 7.6),
    },
    "Brinjal": {
        "temperature": (46.2, 46.5, 47.9, 48.2),
        "rainfall":    (1437.2, 1445.9, 1490.5, 1499.2),
        "soil_ph":     (7.6, 7.7, 7.8, 7.8),
    },
    "Chili": {
        "temperature": (30.7, 30.9, 32.4, 32.6),
        "rainfall":    (714.0, 722.7, 767.3, 776.0),
        "soil_ph":     (6.9, 6.9, 7.0, 7.0),
    },
    "Cabbage": {
        "temperature": (39.2, 39.4, 40.9, 41.2),
        "rainfall":    (1661.4, 1670.0, 1714.7, 1723.3),
        "soil_ph":     (7.6, 7.6, 7.7, 7.8),
    },
    "Broccoli": {
        "temperature": (43.7, 44.0, 45.4, 45.7),
        "rainfall":    (1196.8, 1205.5, 1250.2, 1258.8),
        "soil_ph":     (7.4, 7.4, 7.6, 7.6),
    },
    "Cucumber": {
        "temperature": (35.1, 35.4, 36.8, 37.1),
        "rainfall":    (1102.6, 1111.3, 1155.9, 1164.6),
        "soil_ph":     (7.3, 7.3, 7.5, 7.5),
    },
    "Pumpkin": {
        "temperature": (49.1, 49.4, 50.8, 51.1),
        "rainfall":    (1567.5, 1576.2, 1620.8, 1629.5),
        "soil_ph":     (7.1, 7.1, 7.2, 7.2),
    },
    "Beans": {
        "temperature": (34.3, 34.6, 36.0, 36.3),
        "rainfall":    (1268.8, 1277.4, 1322.1, 1330.8),
        "soil_ph":     (7.3, 7.4, 7.5, 7.5),
    },
    "Peanut": {
        "temperature": (29.0, 29.2, 30.7, 31.0),
        "rainfall":    (1030.4, 1039.1, 1083.7, 1092.4),
        "soil_ph":     (7.2, 7.2, 7.3, 7.3),
    },
    "Mushroom": {
        "temperature": (27.2, 27.5, 28.9, 29.2),
        "rainfall":    (1148.3, 1156.9, 1201.6, 1210.2),
        "soil_ph":     (7.4, 7.5, 7.6, 7.6),
    },
    "Sugarcane": {
        "temperature": (52.6, 52.9, 54.3, 54.6),
        "rainfall":    (1848.4, 1857.0, 1901.7, 1910.4),
        "soil_ph":     (7.6, 7.6, 7.8, 7.8),
    },
    "Coconut": {
        "temperature": (44.9, 45.2, 46.6, 46.9),
        "rainfall":    (1683.2, 1691.9, 1736.5, 1745.2),
        "soil_ph":     (7.8, 7.8, 8.0, 8.0),
    },
    "Mango": {
        "temperature": (43.2, 43.5, 44.9, 45.2),
        "rainfall":    (1456.6, 1465.3, 1510.0, 1518.6),
        "soil_ph":     (7.5, 7.5, 7.7, 7.7),
    },
    "Banana": {
        "temperature": (40.9, 41.2, 42.8, 43.2),
        "rainfall":    (1515.4, 1524.1, 1568.7, 1577.4),
        "soil_ph":     (7.4, 7.4, 7.5, 7.5),
    },
    "Grapes": {
        "temperature": (37.6, 37.9, 39.5, 39.8),
        "rainfall":    (1218.2, 1226.8, 1271.5, 1280.1),
        "soil_ph":     (7.2, 7.3, 7.4, 7.4),
    },
    "Lemon": {
        "temperature": (32.9, 33.2, 34.6, 34.9),
        "rainfall":    (954.3, 963.0, 1007.6, 1016.3),
        "soil_ph":     (7.0, 7.0, 7.2, 7.2),
    },
    "Watermelon": {
        "temperature": (49.9, 50.2, 51.6, 51.9),
        "rainfall":    (1599.8, 1608.5, 1653.1, 1661.8),
        "soil_ph":     (7.2, 7.2, 7.3, 7.4),
    },
    "Apple": {
        "temperature": (36.2, 36.5, 38.1, 38.4),
        "rainfall":    (1257.2, 1265.9, 1310.5, 1319.2),
        "soil_ph":     (7.5, 7.5, 7.6, 7.6),
    },
}

DEFAULT_RANGES = {
    "temperature": (10, 20, 30, 40),
    "rainfall":    (400, 700, 1500, 2500),
    "soil_ph":     (5.5, 6.0, 7.5, 8.5),
}

IDEAL_CONDITIONS: dict[str, dict] = {
"Wheat": {
        "min_temp":       17.7,
        "max_temp":       37.5,
        "min_rainfall":   468.5,
        "max_rainfall":   1211.0,
        "ideal_ph_range": (5.9, 8.1),
    },
    "Potato": {
        "min_temp":       17.4,
        "max_temp":       37.5,
        "min_rainfall":   495.5,
        "max_rainfall":   1243.8,
        "ideal_ph_range": (5.8, 8.2),
    },
    "Maize": {
        "min_temp":       17.4,
        "max_temp":       37.7,
        "min_rainfall":   470.6,
        "max_rainfall":   1228.8,
        "ideal_ph_range": (5.8, 8.1),
    },
    "Tomato": {
        "min_temp":       17.3,
        "max_temp":       37.3,
        "min_rainfall":   481.9,
        "max_rainfall":   1232.3,
        "ideal_ph_range": (5.9, 8.2),
    },
    "Rice": {
        "min_temp":       17.4,
        "max_temp":       37.7,
        "min_rainfall":   466.1,
        "max_rainfall":   1220.9,
        "ideal_ph_range": (5.9, 8.2),
    },
    "Onion": {
        "min_temp":       33.2,
        "max_temp":       34.6,
        "min_rainfall":   1056.8,
        "max_rainfall":   1101.4,
        "ideal_ph_range": (7.2, 7.3),
    },
    "Garlic": {
        "min_temp":       31.5,
        "max_temp":       32.9,
        "min_rainfall":   914.1,
        "max_rainfall":   958.7,
        "ideal_ph_range": (7.1, 7.2),
    },
    "Carrot": {
        "min_temp":       37.4,
        "max_temp":       38.9,
        "min_rainfall":   978.3,
        "max_rainfall":   1022.9,
        "ideal_ph_range": (7.5, 7.6),
    },
    "Brinjal": {
        "min_temp":       46.5,
        "max_temp":       47.9,
        "min_rainfall":   1445.9,
        "max_rainfall":   1490.5,
        "ideal_ph_range": (7.7, 7.8),
    },
    "Chili": {
        "min_temp":       30.9,
        "max_temp":       32.4,
        "min_rainfall":   722.7,
        "max_rainfall":   767.3,
        "ideal_ph_range": (6.9, 7.0),
    },
    "Cabbage": {
        "min_temp":       39.4,
        "max_temp":       40.9,
        "min_rainfall":   1670.0,
        "max_rainfall":   1714.7,
        "ideal_ph_range": (7.6, 7.7),
    },
    "Broccoli": {
        "min_temp":       44.0,
        "max_temp":       45.4,
        "min_rainfall":   1205.5,
        "max_rainfall":   1250.2,
        "ideal_ph_range": (7.4, 7.6),
    },
    "Cucumber": {
        "min_temp":       35.4,
        "max_temp":       36.8,
        "min_rainfall":   1111.3,
        "max_rainfall":   1155.9,
        "ideal_ph_range": (7.3, 7.5),
    },
    "Pumpkin": {
        "min_temp":       49.4,
        "max_temp":       50.8,
        "min_rainfall":   1576.2,
        "max_rainfall":   1620.8,
        "ideal_ph_range": (7.1, 7.2),
    },
    "Beans": {
        "min_temp":       34.6,
        "max_temp":       36.0,
        "min_rainfall":   1277.4,
        "max_rainfall":   1322.1,
        "ideal_ph_range": (7.4, 7.5),
    },
    "Peanut": {
        "min_temp":       29.2,
        "max_temp":       30.7,
        "min_rainfall":   1039.1,
        "max_rainfall":   1083.7,
        "ideal_ph_range": (7.2, 7.3),
    },
    "Mushroom": {
        "min_temp":       27.5,
        "max_temp":       28.9,
        "min_rainfall":   1156.9,
        "max_rainfall":   1201.6,
        "ideal_ph_range": (7.5, 7.6),
    },
    "Sugarcane": {
        "min_temp":       52.9,
        "max_temp":       54.3,
        "min_rainfall":   1857.0,
        "max_rainfall":   1901.7,
        "ideal_ph_range": (7.6, 7.8),
    },
    "Coconut": {
        "min_temp":       45.2,
        "max_temp":       46.6,
        "min_rainfall":   1691.9,
        "max_rainfall":   1736.5,
        "ideal_ph_range": (7.8, 8.0),
    },
    "Mango": {
        "min_temp":       43.5,
        "max_temp":       44.9,
        "min_rainfall":   1465.3,
        "max_rainfall":   1510.0,
        "ideal_ph_range": (7.5, 7.7),
    },
    "Banana": {
        "min_temp":       41.2,
        "max_temp":       42.8,
        "min_rainfall":   1524.1,
        "max_rainfall":   1568.7,
        "ideal_ph_range": (7.4, 7.5),
    },
    "Grapes": {
        "min_temp":       37.9,
        "max_temp":       39.5,
        "min_rainfall":   1226.8,
        "max_rainfall":   1271.5,
        "ideal_ph_range": (7.3, 7.4),
    },
    "Lemon": {
        "min_temp":       33.2,
        "max_temp":       34.6,
        "min_rainfall":   963.0,
        "max_rainfall":   1007.6,
        "ideal_ph_range": (7.0, 7.2),
    },
    "Watermelon": {
        "min_temp":       50.2,
        "max_temp":       51.6,
        "min_rainfall":   1608.5,
        "max_rainfall":   1653.1,
        "ideal_ph_range": (7.2, 7.3),
    },
    "Apple": {
        "min_temp":       36.5,
        "max_temp":       38.1,
        "min_rainfall":   1265.9,
        "max_rainfall":   1310.5,
        "ideal_ph_range": (7.5, 7.6),
    },
}


def _stress_factor(value: float, mn: float, ideal_min: float, ideal_max: float, mx: float) -> float:
    """Returns a stress multiplier in [0.0, 1.0]."""
    if ideal_min <= value <= ideal_max:
        return 1.0
    if mn <= value < ideal_min:
        return 0.5 + 0.5 * (value - mn) / (ideal_min - mn + 1e-9)
    if ideal_max < value <= mx:
        return 0.5 + 0.5 * (mx - value) / (mx - ideal_max + 1e-9)
    return 0.0


def _temperature_penalty(temp: float, ranges: dict) -> tuple[float, str | None]:
    """Returns (penalty_fraction, warning)."""
    mn, ideal_min, ideal_max, mx = ranges["temperature"]
    warning = None

    if ideal_min <= temp <= ideal_max:
        return 0.0, None

    if temp < ideal_min:
        if temp < mn:
            penalty = 0.30
            warning = f"Temperature {temp}°C is below the survivable minimum ({mn}°C). Severe cold stress. Yield reduced 30%."
        else:
            ratio = (ideal_min - temp) / (ideal_min - mn + 1e-9)
            penalty = 0.10 + 0.20 * ratio
            warning = f"Temperature {temp}°C is too cold (ideal: {ideal_min}–{ideal_max}°C). Yield reduced ~{penalty*100:.0f}%."

    else:
        if temp > mx:
            penalty = 0.30
            warning = f"Temperature {temp}°C exceeds the survivable maximum ({mx}°C). Severe heat stress. Yield reduced 30%."
        else:
            ratio = (temp - ideal_max) / (mx - ideal_max + 1e-9)
            penalty = 0.10 + 0.20 * ratio
            warning = f"Temperature {temp}°C is too hot (ideal: {ideal_min}–{ideal_max}°C). Yield reduced ~{penalty*100:.0f}%."

    return round(penalty, 4), warning


def _rainfall_penalty(rain: float, ranges: dict) -> tuple[float, str | None]:
    """Returns (penalty_fraction, warning)."""
    _, _, ideal_max, mx = ranges["rainfall"]

    if rain > mx:
        return 0.15, (
            f"Rainfall {rain}mm is excessively high (max viable: {mx}mm). "
            f"Risk of waterlogging and root rot. Yield reduced 15%."
        )
    if rain > ideal_max:
        return 0.15, (
            f"Rainfall {rain}mm exceeds the ideal range (ideal max: {ideal_max}mm). "
            f"Moderate waterlogging risk. Yield reduced 15%."
        )
    return 0.0, None


def _ph_penalty(ph: float, ranges: dict) -> tuple[float, str | None]:
    """Returns (penalty_fraction, warning)."""
    _, ideal_min, ideal_max, _ = ranges["soil_ph"]

    if ph < ideal_min:
        return 0.10, (
            f"Soil pH {ph} is below the ideal range ({ideal_min}–{ideal_max}). "
            f"Nutrient deficiencies likely. Yield reduced 10%."
        )
    if ph > ideal_max:
        return 0.10, (
            f"Soil pH {ph} is above the ideal range ({ideal_min}–{ideal_max}). "
            f"Micronutrient lockout possible. Yield reduced 10%."
        )
    return 0.0, None


def _risk_from_loss(loss_pct: float) -> str:
    """Classify risk level based on total yield loss percentage."""
    if loss_pct <= 0.10:
        return "Low"
    elif loss_pct <= 0.30:
        return "Medium"
    else:
        return "High"


def analyze_environment(
    input_data: dict[str, Any],
    crop_name: str,
    predicted_yield: float
) -> dict[str, Any]:
    """Adjusts predicted yield based on environmental stress penalties."""
    ranges = CROP_RANGES.get(crop_name, DEFAULT_RANGES)

    temperature = float(input_data.get("Temperature_C", 27.0))
    rainfall    = float(input_data.get("Rainfall_mm", 850.0))
    soil_ph     = float(input_data.get("Soil_pH", 7.0))

    temp_p, temp_warn = _temperature_penalty(temperature, ranges)
    rain_p, rain_warn = _rainfall_penalty(rainfall, ranges)
    ph_p,   ph_warn   = _ph_penalty(soil_ph, ranges)

    retention = (1 - temp_p) * (1 - rain_p) * (1 - ph_p)
    adjusted_yield = round(predicted_yield * retention, 3)

    total_loss = 1 - retention
    risk_level = _risk_from_loss(total_loss)

    warnings = [w for w in [temp_warn, rain_warn, ph_warn] if w]

    return {
        "adjusted_yield": adjusted_yield,
        "risk_level":     risk_level,
        "warnings":       warnings
    }


def generate_advisories(input_data: dict[str, Any], crop_name: str) -> list[str]:
    """Generates farmer-friendly actionable advisory messages based on farm conditions."""
    advisories: list[str] = []
    ranges = CROP_RANGES.get(crop_name, DEFAULT_RANGES)
    ideal  = IDEAL_CONDITIONS.get(crop_name, {})

    temp       = float(input_data.get("Temperature_C", 27.0))
    rainfall   = float(input_data.get("Rainfall_mm", 850.0))
    soil_ph    = float(input_data.get("Soil_pH", 7.0))
    irrigation = str(input_data.get("Irrigation_Type", "")).lower()
    fertilizer = float(input_data.get("Fertilizer_Used_kg", 110.0))
    soil_type  = str(input_data.get("Soil_Type", "")).lower()
    season     = str(input_data.get("Season", "")).lower()

    _, ideal_min_temp, ideal_max_temp, _ = ranges["temperature"]
    _, _, ideal_max_rain, max_rain       = ranges["rainfall"]
    _, ideal_min_ph, ideal_max_ph, _     = ranges["soil_ph"]

    if temp > ideal_max_temp:
        advisories.append(
            "🌡️ High temperature detected. Consider mulching to retain soil moisture "
            "and reduce surface heat stress on roots."
        )
        if temp > ideal_max_temp + 5:
            advisories.append(
                "☀️ Extreme heat alert. Use shade nets or row covers during peak afternoon "
                "hours to protect crops from scorching."
            )
    elif temp < ideal_min_temp:
        advisories.append(
            "🥶 Low temperature detected. Use frost covers or plastic mulch at night "
            "to retain ground warmth and protect seedlings."
        )
        if temp < ideal_min_temp - 5:
            advisories.append(
                "❄️ Frost risk. Delay sowing until temperatures stabilize. "
                "Consider a greenhouse start for seedlings."
            )

    if rainfall > max_rain:
        advisories.append(
            "🌧️ Excessive rainfall. Reduce irrigation frequency and ensure proper "
            "field drainage to prevent waterlogging and root rot."
        )
        advisories.append(
            "💧 Consider creating raised beds or drainage channels to channel "
            "excess water away from the root zone."
        )
    elif rainfall > ideal_max_rain:
        advisories.append(
            "🌦️ Above-ideal rainfall. Reduce irrigation frequency and monitor "
            "fields for early signs of waterlogging."
        )
    elif rainfall < ranges["rainfall"][0]:
        advisories.append(
            "🏜️ Critically low rainfall. Increase irrigation frequency and consider "
            "drip irrigation to conserve water and maintain root moisture."
        )

    if soil_ph < ideal_min_ph:
        advisories.append(
            f"🧪 Soil is too acidic (pH {soil_ph}). Apply agricultural lime (calcium "
            f"carbonate) to raise pH towards the ideal range of {ideal_min_ph}–{ideal_max_ph}."
        )
    elif soil_ph > ideal_max_ph:
        advisories.append(
            f"🧪 Soil is too alkaline (pH {soil_ph}). Apply elemental sulfur or "
            f"acidifying fertilizers to lower pH towards {ideal_min_ph}–{ideal_max_ph}."
        )

    if rainfall > ideal_max_rain and irrigation == "flood":
        advisories.append(
            "🚿 Switch from flood irrigation to drip or sprinkler systems during "
            "high-rainfall periods to avoid over-saturation."
        )
    if irrigation == "rainfed" and rainfall < ranges["rainfall"][0]:
        advisories.append(
            "💦 Rainfed irrigation is insufficient under current drought conditions. "
            "Install supplemental drip or sprinkler irrigation urgently."
        )

    if fertilizer > 180:
        advisories.append(
            "⚗️ Fertilizer usage is very high. Excess nitrogen can cause leaf burn "
            "and runoff pollution. Consider a split application schedule."
        )
    elif fertilizer < 40:
        advisories.append(
            f"🌿 Fertilizer level is low for {crop_name}. Increase application "
            f"gradually and consider a soil nutrient test before the next season."
        )

    if soil_type == "sandy":
        advisories.append(
            "🪨 Sandy soil drains quickly. Add organic compost or mulch to improve "
            "water retention and nutrient-holding capacity."
        )
    elif soil_type == "clay":
        advisories.append(
            "🟤 Clay soil retains excess moisture. Improve aeration by adding "
            "organic matter or sand to prevent compaction and root rot."
        )
    elif soil_type == "peaty":
        advisories.append(
            "🌱 Peaty soil is naturally acidic. Monitor pH closely and apply lime "
            "periodically, especially for pH-sensitive crops."
        )

    if "summer" in season and crop_name in ("Wheat", "Potato"):
        advisories.append(
            f"📅 {crop_name} is generally not ideal for summer growing. "
            f"Consider switching to a Rabi or Kharif season for better yield."
        )
    if "kharif" in season and crop_name == "Potato":
        advisories.append(
            "📅 Potato performs best in Rabi season (cool weather). "
            "Kharif planting may reduce tuber quality and yield."
        )

    if not advisories:
        advisories.append(
            f"✅ Farm conditions look good for {crop_name}. "
            f"Maintain current practices and monitor the crop weekly."
        )

    return advisories

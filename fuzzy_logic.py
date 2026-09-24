import numpy as np
import skfuzzy as fuzz


# Input ranges
temperature = np.arange(0, 46, 1)
moisture = np.arange(0, 101, 1)
soil_ph = np.arange(3, 10.1, 0.1)
rainfall = np.arange(0, 2001, 1)

# Output range
suitability = np.arange(0, 101, 1)


# Temperature membership functions
temp_low = fuzz.trimf(temperature, [0, 0, 20])
temp_medium = fuzz.trimf(temperature, [15, 25, 35])
temp_high = fuzz.trimf(temperature, [30, 45, 45])


# Soil moisture membership functions
moisture_dry = fuzz.trimf(moisture, [0, 0, 40])
moisture_medium = fuzz.trimf(moisture, [20, 50, 80])
moisture_wet = fuzz.trimf(moisture, [60, 100, 100])


# Soil pH membership functions
ph_acidic = fuzz.trimf(soil_ph, [3, 3, 6])
ph_neutral = fuzz.trimf(soil_ph, [5.5, 6.8, 8])
ph_alkaline = fuzz.trimf(soil_ph, [7, 10, 10])


# Rainfall membership functions
rain_low = fuzz.trimf(rainfall, [0, 0, 600])
rain_medium = fuzz.trimf(rainfall, [400, 900, 1400])
rain_high = fuzz.trimf(rainfall, [1000, 2000, 2000])


# Suitability membership functions
suit_low = fuzz.trimf(suitability, [0, 0, 40])
suit_medium = fuzz.trimf(suitability, [25, 50, 75])
suit_high = fuzz.trimf(suitability, [60, 100, 100])


def calculate_suitability(
    temp_value,
    moisture_value,
    ph_value,
    rainfall_value
):

    # Fuzzification - Temperature
    temp_low_degree = fuzz.interp_membership(
        temperature, temp_low, temp_value
    )

    temp_medium_degree = fuzz.interp_membership(
        temperature, temp_medium, temp_value
    )

    temp_high_degree = fuzz.interp_membership(
        temperature, temp_high, temp_value
    )

    # Fuzzification - Moisture
    moisture_dry_degree = fuzz.interp_membership(
        moisture, moisture_dry, moisture_value
    )

    moisture_medium_degree = fuzz.interp_membership(
        moisture, moisture_medium, moisture_value
    )

    moisture_wet_degree = fuzz.interp_membership(
        moisture, moisture_wet, moisture_value
    )

    # Fuzzification - pH
    ph_acidic_degree = fuzz.interp_membership(
        soil_ph, ph_acidic, ph_value
    )

    ph_neutral_degree = fuzz.interp_membership(
        soil_ph, ph_neutral, ph_value
    )

    ph_alkaline_degree = fuzz.interp_membership(
        soil_ph, ph_alkaline, ph_value
    )

    # Fuzzification - Rainfall
    rain_low_degree = fuzz.interp_membership(
        rainfall, rain_low, rainfall_value
    )

    rain_medium_degree = fuzz.interp_membership(
        rainfall, rain_medium, rainfall_value
    )

    rain_high_degree = fuzz.interp_membership(
        rainfall, rain_high, rainfall_value
    )

    # -------------------------
    # Fuzzy Rules
    # -------------------------

    # Rule 1
    # Medium temperature + medium moisture
    # + neutral pH + medium rainfall = High
    rule1 = min(
        temp_medium_degree,
        moisture_medium_degree,
        ph_neutral_degree,
        rain_medium_degree
    )

    # Rule 2
    # High temperature + wet soil + high rainfall = High
    rule2 = min(
        temp_high_degree,
        moisture_wet_degree,
        rain_high_degree
    )

    # Rule 3
    # Dry soil + low rainfall = Low
    rule3 = min(
        moisture_dry_degree,
        rain_low_degree
    )

    # Rule 4
    # Acidic soil + dry soil = Low
    rule4 = min(
        ph_acidic_degree,
        moisture_dry_degree
    )

    # Rule 5
    # Neutral pH + medium moisture
    # + medium rainfall = High
    rule5 = min(
        ph_neutral_degree,
        moisture_medium_degree,
        rain_medium_degree
    )

    # Rule activation
    low_activation = max(rule3, rule4)
    high_activation = max(rule1, rule2, rule5)

    # Apply activated output membership functions
    low_output = np.fmin(
        low_activation,
        suit_low
    )

    high_output = np.fmin(
        high_activation,
        suit_high
    )

    # Aggregate outputs
    aggregated = np.fmax(
        low_output,
        high_output
    )

    # Defuzzification using centroid method
    score = fuzz.defuzz(
        suitability,
        aggregated,
        'centroid'
    )

    return round(score, 2)
# Indigenous Knowledge System (IKS) - Agriculture Knowledge

IKS_PRACTICES = {
    "Rice": {
        "practice": "Seasonal and water-aware cultivation",
        "knowledge": (
            "Traditional agricultural knowledge often considers "
            "seasonal rainfall, water availability and local soil "
            "conditions when planning rice cultivation."
        ),
        "modern_connection": (
            "The Smart Agriculture Crop Advisor uses rainfall, "
            "soil moisture, temperature and soil pH as measurable "
            "environmental factors."
        )
    },

    "Wheat": {
        "practice": "Season-based crop selection",
        "knowledge": (
            "Traditional farming decision-making considers seasonal "
            "temperature and water availability when selecting crops."
        ),
        "modern_connection": (
            "The system uses temperature, rainfall, soil moisture "
            "and soil pH to evaluate crop suitability."
        )
    },

    "Maize": {
        "practice": "Local soil and water resource consideration",
        "knowledge": (
            "Traditional agricultural systems consider available "
            "water, soil characteristics and local climate when "
            "selecting suitable crops."
        ),
        "modern_connection": (
            "The fuzzy system combines several environmental "
            "parameters instead of relying on only one condition."
        )
    },

    "Cotton": {
        "practice": "Observation of local soil and climate",
        "knowledge": (
            "Traditional farming knowledge considers local climate, "
            "soil condition and rainfall before crop selection."
        ),
        "modern_connection": (
            "The project converts these environmental factors "
            "into measurable inputs for a computational "
            "decision-support system."
        )
    },

    "Sugarcane": {
        "practice": "Water and soil resource management",
        "knowledge": (
            "Agricultural knowledge emphasizes matching water "
            "availability and soil conditions with crop requirements."
        ),
        "modern_connection": (
            "The system evaluates rainfall, soil moisture, "
            "temperature and soil pH before recommending crops."
        )
    },

    "Soybean": {
        "practice": "Season and soil-based crop selection",
        "knowledge": (
            "Traditional agricultural decision-making considers "
            "seasonal conditions and local soil characteristics."
        ),
        "modern_connection": (
            "The fuzzy system evaluates multiple environmental "
            "conditions together and produces a gradual "
            "crop suitability score."
        )
    }
}


def get_iks_data():
    return IKS_PRACTICES
# Crop information for Smart Agriculture Crop Advisor

CROPS = {
    "Rice": {
        "temperature": (20, 35),
        "moisture": (60, 90),
        "soil_ph": (5.5, 7.0),
        "rainfall": (1000, 2000),
        "description": "Rice needs warm temperature, high soil moisture and high rainfall."
    },

    "Wheat": {
        "temperature": (15, 25),
        "moisture": (40, 70),
        "soil_ph": (6.0, 7.5),
        "rainfall": (400, 1000),
        "description": "Wheat grows well in cool to moderate temperatures with moderate rainfall."
    },

    "Maize": {
        "temperature": (18, 32),
        "moisture": (40, 75),
        "soil_ph": (5.5, 7.5),
        "rainfall": (500, 1200),
        "description": "Maize prefers warm temperatures, moderate moisture and moderate rainfall."
    },

    "Cotton": {
        "temperature": (21, 35),
        "moisture": (40, 70),
        "soil_ph": (5.5, 8.0),
        "rainfall": (500, 1000),
        "description": "Cotton prefers warm temperatures and moderate rainfall."
    },

    "Sugarcane": {
        "temperature": (20, 35),
        "moisture": (60, 90),
        "soil_ph": (6.0, 7.5),
        "rainfall": (1000, 2000),
        "description": "Sugarcane requires warm weather, good moisture and high rainfall."
    },

    "Soybean": {
        "temperature": (20, 30),
        "moisture": (50, 80),
        "soil_ph": (6.0, 7.5),
        "rainfall": (600, 1200),
        "description": "Soybean grows well in warm conditions with moderate moisture and rainfall."
    }
}


def get_crop_data():
    return CROPS
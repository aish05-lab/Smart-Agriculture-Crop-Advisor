import streamlit as st
import pandas as pd

from llm_parser import extract_farm_data
from fuzzy_logic import calculate_suitability
from crop_data import get_crop_data


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Agriculture Crop Advisor",
    page_icon="🌱",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background-color: #0B2E1A;
        color: #FFFFFF;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #FFFFFF;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #D8F3DC;
        margin-bottom: 30px;
    }

    /* Normal text */
    .stApp p,
    .stApp label,
    .stApp span,
    .stApp div {
        color: #FFFFFF;
    }

    /* Input box */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 2px solid #52B788;
        border-radius: 10px;
    }

    /* Input placeholder */
    .stTextArea textarea::placeholder {
        color: #555555 !important;
    }

    /* Information box */
    .info-box {
        padding: 18px;
        border-radius: 12px;
        background-color: #163D26;
        border: 1px solid #52B788;
        margin-bottom: 20px;
        color: #FFFFFF !important;
    }

    /* Crop cards */
    .crop-card {
        padding: 18px;
        border-radius: 12px;
        background-color: #163D26;
        border: 1px solid #52B788;
        margin-bottom: 12px;
        color: #FFFFFF !important;
    }

    .crop-card h3 {
        color: #95D5B2 !important;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background-color: #163D26;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #52B788;
    }

    [data-testid="stMetricLabel"] {
        color: #D8F3DC !important;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }

    /* Button */
    .stButton > button {
        background-color: #2D6A4F;
        color: #FFFFFF !important;
        border: 1px solid #74C69D;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
    }

    .stButton > button:hover {
        background-color: #40916C;
        color: #FFFFFF !important;
    }

    /* Dataframe */
    [data-testid="stDataFrame"] {
        background-color: #FFFFFF;
    }

    /* Info / success / warning boxes */
    .stAlert {
        color: #FFFFFF !important;
    }

    /* Footer */
    .stCaption {
        color: #B7E4C7 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)
# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🌱 Smart Agriculture Crop Advisor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI + Fuzzy Logic based Crop Recommendation System'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# PROJECT DESCRIPTION
# =========================================================

st.markdown(
    """
    <div class="info-box">

    <b>How it works:</b><br><br>

    👨‍🌾 Farmer enters farm information in natural language<br>
    ↓<br>
    🤖 Gemini + LangChain extracts agricultural parameters<br>
    ↓<br>
    🧠 Fuzzy Logic evaluates farm suitability<br>
    ↓<br>
    🌾 System recommends suitable crops

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FARM INPUT
# =========================================================

st.subheader("👨‍🌾 Enter Your Farm Information")

user_input = st.text_area(
    "Describe your farm in simple language:",
    placeholder=(
        "Example: My farm temperature is 28°C, "
        "soil moisture is 60%, soil pH is 6.5 "
        "and annual rainfall is 800 mm."
    ),
    height=130
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button(
    "🔍 Analyze Farm",
    use_container_width=True
):

    if not user_input.strip():

        st.warning(
            "Please enter your farm information first."
        )

    else:

        try:

            # -------------------------------------------------
            # STEP 1: AI / LANGCHAIN
            # -------------------------------------------------

            with st.spinner(
                "🤖 AI is understanding your farm information..."
            ):

                farm_data = extract_farm_data(
                    user_input
                )


            # -------------------------------------------------
            # STEP 2: DISPLAY EXTRACTED DATA
            # -------------------------------------------------

            st.success(
                "Farm information successfully extracted!"
            )

            st.subheader(
                "📊 Extracted Farm Parameters"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "🌡️ Temperature",
                    f"{farm_data['temperature']:.1f} °C"
                )

            with col2:
                st.metric(
                    "💧 Soil Moisture",
                    f"{farm_data['moisture']:.1f} %"
                )

            with col3:
                st.metric(
                    "🧪 Soil pH",
                    f"{farm_data['soil_ph']:.1f}"
                )

            with col4:
                st.metric(
                    "🌧️ Rainfall",
                    f"{farm_data['rainfall']:.1f} mm"
                )


            # -------------------------------------------------
            # STEP 3: FUZZY LOGIC
            # -------------------------------------------------

            with st.spinner(
                "🧠 Fuzzy inference system is evaluating suitability..."
            ):

                suitability = calculate_suitability(
                    farm_data["temperature"],
                    farm_data["moisture"],
                    farm_data["soil_ph"],
                    farm_data["rainfall"]
                )


            # -------------------------------------------------
            # STEP 4: SUITABILITY SCORE
            # -------------------------------------------------

            st.subheader(
                "🧠 Overall Farm Suitability"
            )

            score_col1, score_col2 = st.columns(
                [1, 2]
            )

            with score_col1:

                st.metric(
                    "Suitability Score",
                    f"{suitability:.2f} / 100"
                )

            with score_col2:

                st.progress(
                    min(int(suitability), 100)
                )


            # -------------------------------------------------
            # STEP 5: CROP RECOMMENDATION
            # -------------------------------------------------

            st.subheader(
                "🌾 Recommended Crops"
            )

            crops = get_crop_data()

            crop_results = []


            for crop_name, crop in crops.items():

                score = 0

                # Temperature
                temp_min, temp_max = crop[
                    "temperature"
                ]

                if (
                    temp_min
                    <= farm_data["temperature"]
                    <= temp_max
                ):
                    score += 25


                # Moisture
                moisture_min, moisture_max = crop[
                    "moisture"
                ]

                if (
                    moisture_min
                    <= farm_data["moisture"]
                    <= moisture_max
                ):
                    score += 25


                # Soil pH
                ph_min, ph_max = crop[
                    "soil_ph"
                ]

                if (
                    ph_min
                    <= farm_data["soil_ph"]
                    <= ph_max
                ):
                    score += 25


                # Rainfall
                rain_min, rain_max = crop[
                    "rainfall"
                ]

                if (
                    rain_min
                    <= farm_data["rainfall"]
                    <= rain_max
                ):
                    score += 25


                crop_results.append(
                    {
                        "Crop": crop_name,
                        "Match Score": score,
                        "Description": crop[
                            "description"
                        ]
                    }
                )


            # Sort crops by score
            crop_results = sorted(
                crop_results,
                key=lambda x: x["Match Score"],
                reverse=True
            )


            # -------------------------------------------------
            # STEP 6: DISPLAY TOP CROPS
            # -------------------------------------------------

            top_crops = crop_results[:3]

            for index, crop in enumerate(
                top_crops
            ):

                st.markdown(
                    f"""
                    <div class="crop-card">

                    <h3>
                    🌾 {index + 1}. {crop['Crop']}
                    </h3>

                    <b>Crop Match:</b>
                    {crop['Match Score']} / 100

                    <br><br>

                    {crop['Description']}

                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # -------------------------------------------------
            # STEP 7: RESULTS TABLE
            # -------------------------------------------------

            st.subheader(
                "📋 Crop Comparison"
            )

            table_data = []

            for crop in crop_results:

                table_data.append(
                    {
                        "Crop": crop["Crop"],
                        "Match Score": crop[
                            "Match Score"
                        ]
                    }
                )

            df = pd.DataFrame(
                table_data
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )


            # -------------------------------------------------
            # FINAL MESSAGE
            # -------------------------------------------------

            st.info(
                "ℹ️ The recommendation is generated "
                "using the extracted farm conditions "
                "and the fuzzy inference system."
            )


        except Exception as e:

            st.error(
                "❌ Something went wrong while "
                "analyzing the farm."
            )

            st.exception(e)


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "Smart Agriculture Crop Advisor | "
    "AI + LangChain + Gemini + Fuzzy Logic + Streamlit"
)
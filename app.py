import streamlit as st
import pandas as pd

from llm_parser import extract_farm_data
from fuzzy_logic import calculate_suitability
from crop_data import get_crop_data
from iks_data import get_iks_data


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

    /* Main heading */
    h1 {
        color: #FFFFFF !important;
        font-weight: 700;
    }

    h2, h3 {
        color: #FFFFFF !important;
    }

    /* Normal text */
    p, label, span {
        color: #FFFFFF;
    }

    /* Text area */
    textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #4CAF50 !important;
        border-radius: 10px !important;
    }

    /* Text input */
    input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    /* Button */
    .stButton > button {
        background-color: #2E7D32;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 25px;
        font-size: 17px;
        font-weight: bold;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #43A047;
        color: white;
    }

    /* Cards */
    .info-card {
        background-color: #123D24;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #2E7D32;
        margin-bottom: 15px;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background-color: #123D24;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #2E7D32;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }

    [data-testid="stMetricLabel"] {
        color: #FFFFFF !important;
    }

    /* Dataframe */
    [data-testid="stDataFrame"] {
        background-color: white;
    }

    /* Horizontal line */
    hr {
        border-color: #4CAF50;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TITLE
# =========================================================

st.title("🌱 Smart Agriculture Crop Advisor")

st.markdown(
    """
    ### AI + Fuzzy Logic Based Crop Recommendation System

    This mini project uses **Artificial Intelligence, LangChain,
    Gemini and Fuzzy Logic** to analyze farm conditions and
    recommend suitable crops.

    The system accepts a farmer's description in natural language,
    extracts agricultural parameters using an LLM, evaluates
    suitability using fuzzy inference, and provides crop
    recommendations along with an Indigenous Knowledge System (IKS)
    context.
    """
)

st.divider()


# =========================================================
# USER INPUT
# =========================================================

st.subheader("🧑‍🌾 Enter Your Farm Information")

st.write(
    "Describe your farm conditions in normal language."
)

user_input = st.text_area(
    "Farm Description",
    height=150,
    placeholder=(
        "Example: My farm has a temperature of 28 degrees Celsius, "
        "soil moisture is 60 percent, soil pH is 6.5 and rainfall "
        "is around 800 mm."
    )
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze_button = st.button(
    "🔍 Analyze Farm & Recommend Crops"
)


# =========================================================
# MAIN ANALYSIS
# =========================================================

if analyze_button:

    if not user_input.strip():

        st.warning(
            "⚠️ Please enter your farm information first."
        )

        st.stop()

    try:

        # -------------------------------------------------
        # STEP 1: AI / LLM EXTRACTION
        # -------------------------------------------------

        st.subheader("🤖 AI Analysis")

        with st.spinner(
            "Gemini AI is understanding your farm description..."
        ):

            farm_data = extract_farm_data(user_input)


        st.success(
            "✅ Agricultural parameters extracted successfully!"
        )


        # -------------------------------------------------
        # STEP 2: DISPLAY EXTRACTED VALUES
        # -------------------------------------------------

        st.subheader("📊 Extracted Farm Parameters")

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


        st.divider()


        # -------------------------------------------------
        # STEP 3: FUZZY LOGIC
        # -------------------------------------------------

        st.subheader("🧠 Fuzzy Logic Suitability Analysis")

        with st.spinner(
            "Evaluating farm conditions using fuzzy inference..."
        ):

            suitability_score = calculate_suitability(
                farm_data["temperature"],
                farm_data["moisture"],
                farm_data["soil_ph"],
                farm_data["rainfall"]
            )


        st.metric(
            "🌱 Overall Farm Suitability",
            f"{float(suitability_score):.2f} / 100"
        )


        # Progress bar
        st.progress(
            min(
                max(float(suitability_score) / 100, 0.0),
                1.0
            )
        )


        # Suitability interpretation
        if suitability_score >= 70:

            st.success(
                "🟢 The environmental conditions show high suitability."
            )

        elif suitability_score >= 40:

            st.warning(
                "🟡 The environmental conditions show moderate suitability."
            )

        else:

            st.error(
                "🔴 The environmental conditions show low suitability."
            )


        st.divider()


        # -------------------------------------------------
        # STEP 4: CROP RECOMMENDATION
        # -------------------------------------------------

        st.subheader("🌾 Crop Recommendations")

        crops = get_crop_data()

        crop_results = []


        for crop_name, crop in crops.items():

            score = 0

            # ---------------------------------------------
            # Temperature
            # ---------------------------------------------

            temperature_min = crop["temperature"][0]
            temperature_max = crop["temperature"][1]

            if (
                temperature_min
                <= farm_data["temperature"]
                <= temperature_max
            ):
                score += 25


            # ---------------------------------------------
            # Soil Moisture
            # ---------------------------------------------

            moisture_min = crop["moisture"][0]
            moisture_max = crop["moisture"][1]

            if (
                moisture_min
                <= farm_data["moisture"]
                <= moisture_max
            ):
                score += 25


            # ---------------------------------------------
            # Soil pH
            # ---------------------------------------------

            ph_min = crop["soil_ph"][0]
            ph_max = crop["soil_ph"][1]

            if (
                ph_min
                <= farm_data["soil_ph"]
                <= ph_max
            ):
                score += 25


            # ---------------------------------------------
            # Rainfall
            # ---------------------------------------------

            rainfall_min = crop["rainfall"][0]
            rainfall_max = crop["rainfall"][1]

            if (
                rainfall_min
                <= farm_data["rainfall"]
                <= rainfall_max
            ):
                score += 25


            crop_results.append(
                {
                    "Crop": crop_name,
                    "Match Score": score,
                    "Description": crop["description"]
                }
            )


        # Sort crops from highest to lowest score

        crop_results = sorted(
            crop_results,
            key=lambda x: x["Match Score"],
            reverse=True
        )


        # -------------------------------------------------
        # TOP 3 CROPS
        # -------------------------------------------------

        st.write(
            "### ⭐ Recommended Crops"
        )

        top_crops = crop_results[:3]

        col1, col2, col3 = st.columns(3)

        columns = [col1, col2, col3]

        for index, crop in enumerate(top_crops):

            with columns[index]:

                st.markdown(
                    f"""
                    <div class="info-card">

                    <h3>🌾 {crop['Crop']}</h3>

                    <p>
                    <b>Match Score:</b>
                    {crop['Match Score']} / 100
                    </p>

                    <p>
                    {crop['Description']}
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # -------------------------------------------------
        # COMPLETE CROP TABLE
        # -------------------------------------------------

        st.write(
            "### 📋 Crop Suitability Table"
        )

        crop_dataframe = pd.DataFrame(
            crop_results
        )

        st.dataframe(
            crop_dataframe,
            use_container_width=True,
            hide_index=True
        )


        st.divider()


        # =================================================
        # IKS CONNECTION
        # =================================================

        st.subheader(
            "🇮🇳 Indigenous Knowledge System (IKS) Connection"
        )

        st.write(
            """
            This project connects modern Artificial Intelligence
            and Fuzzy Logic with Indigenous Knowledge System (IKS)
            in agriculture.

            Traditional agricultural decision-making considers
            factors such as seasonal conditions, rainfall,
            water availability and soil characteristics.

            The project represents these ideas using measurable
            environmental parameters such as temperature,
            soil moisture, soil pH and rainfall.
            """
        )


        # -------------------------------------------------
        # IKS DATA
        # -------------------------------------------------

        iks_data = get_iks_data()


        if crop_results:

            top_crop_name = crop_results[0]["Crop"]


            if top_crop_name in iks_data:

                iks = iks_data[top_crop_name]


                st.markdown(
                    f"""
                    <div class="info-card">

                    <h3>🌾 IKS Context for {top_crop_name}</h3>

                    <p>
                    <b>Traditional Knowledge Connection:</b><br>
                    {iks["practice"]}
                    </p>

                    <p>
                    <b>Knowledge Context:</b><br>
                    {iks["knowledge"]}
                    </p>

                    <p>
                    <b>Connection with Modern Technology:</b><br>
                    {iks["modern_connection"]}
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


        st.info(
            """
            ℹ️ The IKS information is provided as a knowledge
            context alongside the AI and fuzzy-logic analysis.
            It does not replace professional agricultural advice.
            """
        )


        st.divider()


        # =================================================
        # WORKFLOW
        # =================================================

        st.subheader("⚙️ System Workflow")

        st.markdown(
            """
            **Step 1:** Farmer enters farm information in natural language.

            ↓

            **Step 2:** Gemini + LangChain understands the text and
            extracts temperature, moisture, soil pH and rainfall.

            ↓

            **Step 3:** The extracted values are passed to the
            Fuzzy Inference System.

            ↓

            **Step 4:** Fuzzy membership functions perform
            fuzzification.

            ↓

            **Step 5:** Fuzzy rules are evaluated and aggregated.

            ↓

            **Step 6:** Centroid defuzzification produces the
            overall suitability score.

            ↓

            **Step 7:** Crop requirements are compared with the
            farm conditions.

            ↓

            **Step 8:** Suitable crops and IKS context are displayed.
            """
        )


    # =====================================================
    # ERROR HANDLING
    # =====================================================

    except Exception as e:

        st.error(
            "❌ An error occurred while analyzing the farm."
        )

        st.exception(e)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center;">

    🌱 <b>Smart Agriculture Crop Advisor</b>

    <br><br>

    AI + LangChain + Gemini + Fuzzy Logic + IKS

    <br>

    Internal Assessment Mini Project

    </div>
    """,
    unsafe_allow_html=True
)
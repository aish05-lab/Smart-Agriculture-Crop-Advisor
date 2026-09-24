import os
import json
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


# ---------------------------------------------------------
# 1. Load Gemini API Key from .env
# ---------------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add your Gemini API key to the .env file."
    )


# ---------------------------------------------------------
# 2. Create Gemini LLM
# ---------------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key,
    temperature=0
)


# ---------------------------------------------------------
# 3. Create Prompt
# ---------------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are an AI assistant for a Smart Agriculture Crop Advisor.

Read the farmer's natural-language description and extract these
four agricultural parameters:

1. temperature - temperature in Celsius
2. moisture - soil moisture percentage
3. soil_ph - soil pH value
4. rainfall - annual rainfall in millimeters

The farmer may provide the information in natural language.

For example:

"My farm has a temperature of 28 degrees Celsius,
soil moisture is 60 percent, pH is 6.5 and rainfall
is around 800 mm."

Return ONLY valid JSON.

Do not add explanations.
Do not add Markdown.
Do not use ```json.

The JSON must have exactly these keys:

{{
    "temperature": number,
    "moisture": number,
    "soil_ph": number,
    "rainfall": number
}}

Farmer's input:
{user_input}
"""
)


# ---------------------------------------------------------
# 4. Create LangChain Chain
# ---------------------------------------------------------

chain = prompt | llm


# ---------------------------------------------------------
# 5. Extract Farm Data
# ---------------------------------------------------------

def extract_farm_data(user_input):

    # Send farmer's natural-language input to Gemini
    response = chain.invoke({
        "user_input": user_input
    })

    # Gemini/LangChain may return content as a string
    # or as a list of content blocks.
    content = response.content

    if isinstance(content, list):

        response_text = ""

        for item in content:

            if isinstance(item, dict):

                if "text" in item:
                    response_text += item["text"]

            else:
                response_text += str(item)

        response_text = response_text.strip()

    else:

        response_text = str(content).strip()


    # -----------------------------------------------------
    # Remove Markdown code blocks if Gemini returns them
    # -----------------------------------------------------

    if response_text.startswith("```"):

        response_text = response_text.replace(
            "```json", ""
        )

        response_text = response_text.replace(
            "```", ""
        )

        response_text = response_text.strip()


    # -----------------------------------------------------
    # Convert JSON text into Python dictionary
    # -----------------------------------------------------

    try:

        data = json.loads(response_text)

    except json.JSONDecodeError:

        raise ValueError(
            "Gemini returned an invalid JSON response:\n"
            + response_text
        )


    # -----------------------------------------------------
    # Check required fields
    # -----------------------------------------------------

    required_keys = [
        "temperature",
        "moisture",
        "soil_ph",
        "rainfall"
    ]

    for key in required_keys:

        if key not in data:

            raise ValueError(
                f"Missing required field: {key}"
            )


    # -----------------------------------------------------
    # Convert values to numbers
    # -----------------------------------------------------

    try:

        data["temperature"] = float(
            data["temperature"]
        )

        data["moisture"] = float(
            data["moisture"]
        )

        data["soil_ph"] = float(
            data["soil_ph"]
        )

        data["rainfall"] = float(
            data["rainfall"]
        )

    except (ValueError, TypeError):

        raise ValueError(
            "Gemini returned non-numeric agricultural values."
        )


    # -----------------------------------------------------
    # Validate ranges
    # -----------------------------------------------------

    if not 0 <= data["temperature"] <= 45:

        raise ValueError(
            "Temperature must be between 0 and 45 °C."
        )

    if not 0 <= data["moisture"] <= 100:

        raise ValueError(
            "Soil moisture must be between 0 and 100%."
        )

    if not 3 <= data["soil_ph"] <= 10:

        raise ValueError(
            "Soil pH must be between 3 and 10."
        )

    if not 0 <= data["rainfall"] <= 2000:

        raise ValueError(
            "Rainfall must be between 0 and 2000 mm."
        )


    # -----------------------------------------------------
    # Return final structured data
    # -----------------------------------------------------

    return data
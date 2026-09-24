# 🌱 Smart Agriculture Crop Advisor

## AI + Fuzzy Logic Mini Project

Smart Agriculture Crop Advisor is an intelligent agriculture application that recommends suitable crops based on farm conditions.

The system combines:

- Artificial Intelligence
- Large Language Model (Gemini)
- LangChain
- Fuzzy Logic
- Python
- Streamlit

---

## 🎯 Objective

The objective of this project is to help farmers identify suitable crops based on:

- Temperature
- Soil Moisture
- Soil pH
- Rainfall

The farmer can enter the information using normal natural language.

For example:

"My farm temperature is 28°C, soil moisture is 60%, soil pH is 6.5 and rainfall is 800 mm."

The AI extracts the required agricultural parameters and the fuzzy inference system evaluates the farm conditions.

---

## 🏗️ System Architecture

Farmer Natural Language Input
        ↓
Gemini LLM + LangChain
        ↓
Farm Parameter Extraction
        ↓
Fuzzification
        ↓
Fuzzy Rule Evaluation
        ↓
Aggregation
        ↓
Defuzzification
        ↓
Suitability Score
        ↓
Crop Recommendation

---

## 🤖 AI / LLM Component

The project uses Google's Gemini Large Language Model through LangChain.

The LLM understands the farmer's natural-language input and extracts:

- Temperature
- Soil moisture
- Soil pH
- Rainfall

Example:

Input:

"My farm is warm at 28 degrees, moisture is 60%, pH is 6.5 and rainfall is 800 mm."

Output:

```json
{
    "temperature": 28,
    "moisture": 60,
    "soil_ph": 6.5,
    "rainfall": 800
}
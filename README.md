# 🌱 Smart Agriculture Crop Advisor

## AI + Fuzzy Logic Based Smart Agriculture Recommendation System

### 👩‍💻 Student Details

**Student Name:** Aishwarya Ambre  
**Roll Number:** 19002  
**Class:** TY IT  
**Academic Year:** 2026–2027  

---

# 1. Project Description

Smart Agriculture Crop Advisor is an AI-based agricultural decision-support system designed to help farmers identify suitable crops based on their farm conditions.

The system accepts information from the farmer in natural language.

For example:

> My farm has a temperature of 28°C, soil moisture is 60%, soil pH is 6.5 and annual rainfall is 800 mm.

The system uses **Gemini LLM with LangChain** to understand the farmer's description and extract important agricultural parameters.

These parameters are then processed using a **Fuzzy Inference System** to calculate the overall suitability of the farm.

The system finally recommends suitable crops based on the farm conditions.

---

# 2. Problem Statement

Farmers need to select crops according to environmental and soil conditions.

However, selecting a suitable crop can be difficult because several factors need to be considered simultaneously, such as:

- Temperature
- Soil moisture
- Soil pH
- Rainfall

Traditional decision-making methods may use fixed values and may not handle uncertainty effectively.

This project provides an intelligent system that combines **AI and Fuzzy Logic** to assist in crop selection.

---

# 3. Objectives

The main objectives of this project are:

1. To develop an AI-based crop recommendation system.
2. To understand natural-language descriptions provided by farmers.
3. To extract agricultural parameters using Gemini and LangChain.
4. To use fuzzy logic for handling uncertain agricultural conditions.
5. To calculate a farm suitability score.
6. To recommend suitable crops.
7. To provide a simple and user-friendly web interface.
8. To deploy the project online.

---

# 4. Main Features

### 🤖 AI Natural Language Understanding

The farmer can enter information using normal language.

Example:

```text
My farm temperature is 28°C, soil moisture is 60%,
soil pH is 6.5 and rainfall is 800 mm.
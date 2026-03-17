# ==========================================
# AIRAWARE SMART - MILESTONE 3 DEMO
# AQI Category & Alert System
# ==========================================

import pandas as pd

# ------------------------------------------
# 1. SAMPLE PREDICTED AQI DATA (from model)
# ------------------------------------------

data = {
    "Date": [
        "2024-01-11",
        "2024-01-12",
        "2024-01-13",
        "2024-01-14",
        "2024-01-15"
    ],
    "Predicted_AQI": [85, 120, 175, 220, 45]
}

df = pd.DataFrame(data)

print("Predicted AQI Data:")
print(df)


# ------------------------------------------
# 2. FUNCTION TO CLASSIFY AQI CATEGORY
# ------------------------------------------

def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


# ------------------------------------------
# 3. APPLY CATEGORY FUNCTION
# ------------------------------------------

df["Category"] = df["Predicted_AQI"].apply(get_aqi_category)

print("\nAQI with Categories:")
print(df)


# ------------------------------------------
# 4. GENERATE ALERTS
# ------------------------------------------

def generate_alert(aqi):
    if aqi > 200:
        return "⚠ HIGH ALERT! Avoid outdoor activities."
    elif aqi > 150:
        return "⚠ Warning! Wear mask outside."
    else:
        return "Air quality is safe."

df["Alert"] = df["Predicted_AQI"].apply(generate_alert)
print("\nFinal Alert Report:")
print(df)

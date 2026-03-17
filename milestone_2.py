# ==========================================
# AIRAWARE SMART - MILESTONE 2 COMPLETE CODE
# AQI Forecasting using Prophet
# ==========================================

# (Run this line ONLY if Prophet is not installed)
# pip install prophet

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet


# ------------------------------------------
# 1. CREATE SAMPLE HISTORICAL AQI DATA
# ------------------------------------------

data = {
    "Date": [
        "2024-01-01","2024-01-02","2024-01-03","2024-01-04",
        "2024-01-05","2024-01-06","2024-01-07","2024-01-08",
        "2024-01-09","2024-01-10"
    ],
    "AQI": [120, 130, 128, 140, 150, 160, 155, 165, 170, 175]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# ------------------------------------------
# 2. PREPROCESSING
# ------------------------------------------

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Rename columns for Prophet compatibility
df = df.rename(columns={"Date": "ds", "AQI": "y"})

print("\nData Prepared for Prophet:")
print(df)


# ------------------------------------------
# 3. CREATE & TRAIN PROPHET MODEL
# ------------------------------------------

model = Prophet()

# Train model using historical data
model.fit(df)


# ------------------------------------------
# 4. CREATE FUTURE DATES FOR PREDICTION
# ------------------------------------------

# Predict next 7 days
future = model.make_future_dataframe(periods=7)

print("\nFuture Dates:")
print(future.tail())


# ------------------------------------------
# 5. MAKE PREDICTIONS
# ------------------------------------------

forecast = model.predict(future)

print("\nPredicted AQI:")
print(forecast[["ds", "yhat"]].tail(7))


# ------------------------------------------
# 6. PLOT FORECAST GRAPH
# ------------------------------------------

model.plot(forecast)
plt.title("Future AQI Prediction")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.show()


# ------------------------------------------
# 7. SHOW TREND & SEASONAL COMPONENTS
# ------------------------------------------

model.plot_components(forecast)
plt.show()

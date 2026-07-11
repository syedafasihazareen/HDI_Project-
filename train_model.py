import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("dataset/hdr_general.csv", encoding="latin1")

# Remove rows with missing values
df = df.dropna(subset=[
    "life_expectancy",
    "mean_yr_school",
    "expec_yr_school",
    "gross_inc_percap",
    "hdi"
])

# Features
X = df[[
    "life_expectancy",
    "mean_yr_school",
    "expec_yr_school",
    "gross_inc_percap"
]]

# Target
y = df["hdi"]

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "model/hdi_model.pkl")

print("Model trained successfully!")
print("Model saved successfully!")
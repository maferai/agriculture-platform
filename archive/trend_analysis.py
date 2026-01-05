import pandas as pd
import numpy as np

# Load historical data
df = pd.read_csv("data/agriculture_6_months_simulated.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# 30-day rolling average
df["water_index_30d_avg"] = df["water_availability_index"].rolling(30).mean()

# Trend slope calculation
trend_slope = np.polyfit(
    range(len(df["water_index_30d_avg"].dropna())),
    df["water_index_30d_avg"].dropna(),
    1
)[0]

# Interpretation
if trend_slope < 0:
    print("⚠️ Declining water availability trend detected.")
else:
    print("✅ Stable or improving water availability trend detected.")

print(f"Trend slope: {trend_slope:.4f}")

import pandas as pd

# Thresholds for crop health classification
HEALTHY_THRESHOLD = 0.95
STRESSED_THRESHOLD = 0.85

# Determine crop health using NDVI values over time
def get_crop_status(ndvi_values):
    average_ndvi = ndvi_values.mean()
    current_ndvi = ndvi_values.iloc[-1]

    if current_ndvi >= HEALTHY_THRESHOLD * average_ndvi:
        return "healthy"
    elif current_ndvi >= STRESSED_THRESHOLD * average_ndvi:
        return "stressed"
    else:
        return "critical"

# NEW: detect NDVI trend
def get_ndvi_trend(ndvi_values):
    start = ndvi_values.iloc[0]
    end = ndvi_values.iloc[-1]

    if end > start:
        return "improving"
    elif end < start:
        return "declining"
    else:
        return "stable"
# Load sample NDVI data
data = pd.read_csv("../data/sample_vegetation.csv")

status = get_crop_status(data["ndvi"])
trend = get_ndvi_trend(data["ndvi"])

average_ndvi = data["ndvi"].mean()
current_ndvi = data["ndvi"].iloc[-1]

print("Average NDVI:", round(average_ndvi, 3))
print("Current NDVI:", round(current_ndvi, 3))
print("Crop status:", status)
print("Vegetation trend:", trend)

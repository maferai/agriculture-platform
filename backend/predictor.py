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

# Load sample NDVI data
data = pd.read_csv("../data/sample_vegetation.csv")

# Classify crop health
status = get_crop_status(data["ndvi"])

print("Crop status:", status)

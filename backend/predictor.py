import pandas as pd

def get_crop_status(ndvi_values):
    average_ndvi = ndvi_values.mean()
    current_ndvi = ndvi_values.iloc[-1]

    if current_ndvi >= 0.95 * average_ndvi:
        return "healthy"
    elif current_ndvi >= 0.85 * average_ndvi:
        return "stressed"
    else:
        return "critical"

data = pd.read_csv("../data/sample_vegetation.csv")
status = get_crop_status(data["ndvi"])

print("Crop status:", status)

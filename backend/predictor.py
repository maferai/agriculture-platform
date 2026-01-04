import pandas as pd

# This function determines crop health using NDVI values over time
def get_crop_status(ndvi_values):
    # Calculate the average NDVI as a baseline reference
    average_ndvi = ndvi_values.mean()

    # Get the most recent NDVI value (current condition)
    current_ndvi = ndvi_values.iloc[-1]

    # Compare current NDVI against the baseline
    if current_ndvi >= 0.95 * average_ndvi:
        return "healthy"
    elif current_ndvi >= 0.85 * average_ndvi:
        return "stressed"
    else:
        return "critical"

# Load sample vegetation data from CSV
data = pd.read_csv("../data/sample_vegetation.csv")

# Classify the crop health status
status = get_crop_status(data["ndvi"])

# Display the result
print("Crop status:", status)

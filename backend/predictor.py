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

# Detect NDVI trend
def get_ndvi_trend(ndvi_values):
    start = ndvi_values.iloc[0]
    end = ndvi_values.iloc[-1]

    if end > start:
        return "improving"
    elif end < start:
        return "declining"
    else:
        return "stable"

# Detect sudden NDVI drop between the last two data points
def detect_sudden_drop(ndvi_values, threshold=0.05):
    """
    Returns True if the NDVI dropped by `threshold` or more since last measurement
    """
    if len(ndvi_values) < 2:
        return False

    return (ndvi_values.iloc[-2] - ndvi_values.iloc[-1]) >= threshold

# Main execution
def main():
    # Load sample NDVI data
    data = pd.read_csv("../data/sample_vegetation.csv")

    # Compute metrics
    status = get_crop_status(data["ndvi"])
    trend = get_ndvi_trend(data["ndvi"])
    alert = detect_sudden_drop(data["ndvi"])

    average_ndvi = data["ndvi"].mean()
    current_ndvi = data["ndvi"].iloc[-1]

    # Output results
    print("Average NDVI:", round(average_ndvi, 3))
    print("Current NDVI:", round(current_ndvi, 3))
    print("Crop status:", status)
    print("Vegetation trend:", trend)
    if alert:
        print("Warning: Sudden NDVI drop detected")

if __name__ == "__main__":
    main()

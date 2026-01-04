import pandas as pd
import matplotlib.pyplot as plt
from backend.predictor import get_crop_status, detect_sudden_drop

# Load NDVI sample data
data = pd.read_csv("../data/sample_vegetation.csv")

# Determine crop status for each week
statuses = data["ndvi"].apply(lambda ndvi: get_crop_status(pd.Series([ndvi])))

# Detect sudden drops week-to-week
alerts = [False] + [detect_sudden_drop(data["ndvi"].iloc[i-1:i+1]) for i in range(1, len(data))]

# Plot NDVI over time
plt.figure(figsize=(10,5))
plt.plot(data["date"], data["ndvi"], label="NDVI", color="green")

# Highlight critical or sudden-drop weeks
for i, (status, alert) in enumerate(zip(statuses, alerts)):
    if status == "critical" or alert:
        plt.scatter(data["date"].iloc[i], data["ndvi"].iloc[i], color="red", s=50, label="Critical / Alert" if i==0 else "")

plt.xlabel("Date")
plt.ylabel("NDVI")
plt.title("Crop Vegetation Health Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

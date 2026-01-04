import pandas as pd
import matplotlib.pyplot as plt

# Load NDVI sample data
data = pd.read_csv("../data/sample_vegetation.csv")

# Plot NDVI over time
plt.plot(data["date"], data["ndvi"])
plt.xlabel("Date")
plt.ylabel("NDVI")
plt.title("Crop Vegetation Health Over Time")

plt.show()

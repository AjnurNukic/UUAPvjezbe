import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

df = pd.read_csv("../vjezbe2/ufo_sightings.csv",low_memory=False)

df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
df = df.dropna(subset=["latitude", "longitude"])

df = df.sample(15000)
plt.figure(figsize=(12,6))
plt.hexbin(
    df["latitude"],
    df["longitude"],
    gridsize=60,
    cmap="viridis",
)
plt.colorbar(label="Sightings density")
plt.title("UFO Sightings Density HeatMap")
plt.xlabel("longitude")
plt.ylabel("latitude")

fig = px.density_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    radius=5,
    zoom=1,
    mapbox_style="open-street-map",
    title="UFO Sightings Density Map",
)
fig.show()
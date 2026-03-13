import pandas as pd
import folium

# Load and clean data
df = pd.read_csv("ufo_sightings.csv", low_memory=False)

df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

df = df.dropna(subset=["latitude", "longitude"])

# Sample for performance
df = df.sample(5000)

# Initialize map
ufo_map = folium.Map(location=[20, 0], zoom_start=2)

# Add markers
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=2,
        popup=row["city"],
        color="red",
    ).add_to(ufo_map)

# Save ONCE at the very end
ufo_map.save("ufo_map.html")
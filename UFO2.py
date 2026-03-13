import pandas as pd
import plotly.express as px

# 1. Load Data
df = pd.read_csv('ufo_sightings.csv')

# 3. Create the Map
# Using scatter_geo is great for a global view
fig = px.scatter_geo(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    title="UFO Sightings Around the World",
)

# 4. Show the Map
fig.show()
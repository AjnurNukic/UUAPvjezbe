import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

df = pd.read_csv("../vjezbe2/ufo_sightings.csv", low_memory=False)

df["datetime"]=pd.to_datetime(df["datetime"], errors="coerce")
df["hour"]=df["datetime"].dt.hour

hour_counts = (
    df["hour"].value_counts().sort_index())
hour_counts.plot(kind="bar")

hour_counts.plot()
plt.title("UFO Sightings")
plt.xlabel("Hour")
plt.ylabel("Sightings")
plt.grid(True)
plt.show()
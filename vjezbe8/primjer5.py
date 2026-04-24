import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
df = pd.read_csv('imdb_top_1000.csv')
plt.figure(figsize=(10, 5))
plt.hist(df["IMDB_Rating"], bins=20, color="steelblue",
         edgecolor="white", alpha=0.8)
plt.title("Distribucija IMDB ocjena (Top 1000)")
plt.xlabel("IMDB Rating")
plt.ylabel("Broj filmova")
plt.axvline(df["IMDB_Rating"].mean(), color="red",
            linestyle="--", label=f"Prosjek: {df['IMDB_Rating'].mean():.2f}")
plt.legend()
plt.tight_layout()
plt.show()
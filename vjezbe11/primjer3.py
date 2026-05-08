import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

sns.set_theme(style="whitegrid")
df = sns.load_dataset("penguins")

sns.histplot(df["flipper_length_mm"], bins=20, kde=True)
plt.show()

sns.histplot(df, x="flipper_length_mm", hue="species", kde=True)
plt.show()

fig, axes = plt.subplots(2,2,figsize=(10,6))
mjere = ["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]

for ax, col in zip(axes.flat, mjere):
    sns.violinplot(data=df, x="species", y=col, ax=ax)
    ax.set_title(col.replace("_", " "))

    plt.suptitle("Mjere pingvina po vrsti")
    plt.tight_layout()
    plt.show()
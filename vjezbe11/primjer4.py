import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

sns.set_theme(style="whitegrid")
df = sns.load_dataset("penguins")

r, p = stats.pearsonr(df["flipper_length_mm"],df["body_mass_g"])
print(f"r = {r:.3f}, p = {p:.4f}")

fig, ax = plt.subplots(figsize=(7,5))
sns.regplot(data=df,x="flipper_length_mm",y="body_mass_g", hue="species",ax=ax)

corr=df.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap="coolwarm",vmin=-1,vmax=1)

sns.pairplot(df,hue="species", diag_kind="kde")
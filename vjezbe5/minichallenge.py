import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

print("Prosječno spavanje po nivou stresa:")
stress_sleep = df.groupby('Stress Level')['Sleep Duration'].mean().sort_values(ascending=False)
print(stress_sleep)

print("\nKvalitet sna po zanimanjima (od najgoreg ka najboljem):")
occ_quality = df.groupby('Occupation')['Quality of Sleep'].mean().sort_values()
print(occ_quality)

stress_sleep.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Prosječno trajanje sna po nivou stresa')
plt.xlabel('Nivo stresa (3 = Najniži, 8 = Najviši)')
plt.ylabel('Sati spavanja')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

occ_quality.plot(kind='barh', color='skyblue', edgecolor='black')
plt.title('Kvalitet sna po zanimanjima')
plt.xlabel('Prosječna ocjena kvaliteta (1-10)')
plt.ylabel('Zanimanje')
plt.tight_layout()
plt.show()
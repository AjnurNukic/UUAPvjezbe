import pandas as pd

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df["Sleep Duration"])
#print(df[["Gender", "Age", "Sleep Duration"]])
#df_females = df[(df['Gender'] == 'Female') & (df['Age'] > 30) & (df['Stress Level'] > 7)]
#print(df_females)
#print(df.loc[df["Sleep Duration"].idxmin()])
#print(df.loc[df["Sleep Duration"].idxmax()])
#osoba_max_hr = df.loc[df["Heart Rate"].idxmax()]
#osoba_min_steps = df.loc[df["Daily Steps"].idxmin()]
#print(osoba_max_hr)
#print(osoba_min_steps)
high_stress = df[df["Stress Level"]>7]
print(high_stress["Sleep Duration"].mean())
low_stress = df[df["Stress Level"]<=3]
print(low_stress["Sleep Duration"].mean())
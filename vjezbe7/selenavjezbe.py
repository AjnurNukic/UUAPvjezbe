import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")
tips.head()
print(tips.head())
result = tips.groupby('day')[['total_bill', 'tip']].agg(['sum', 'mean'])
print("Rezultat", result)

result2=tips.groupby('day')['total_bill'].sum().idxmax()
print("Rezultat 2", result2)
print(pd.pivot_table(tips, values='tip', index='day', columns='time', aggfunc='mean'))
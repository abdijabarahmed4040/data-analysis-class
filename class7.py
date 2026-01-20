import pandas as pd
import numpy as np

df = pd.read_csv("insurance.csv")


print(df.info)

#print(df.describe())
df = df.drop_duplicates()

df['bmi'] = df['bmi'].fillna(df['bmi'].mean())
df['children'] = df['children'].fillna(0)



df['charges_yearly'] = df['charges']
df['charges_monthly'] = df['charges'] / 12

smoker_analysis = df.groupby('smoker').agg(
    avg_charges=('charges', 'mean'),
    max_charges=('charges', 'max'),
    count=('charges', 'count')
)
print(smoker_analysis)

region_summary = df.groupby('region').agg(
    avg_age=('age', 'mean'),
    avg_bmi=('bmi', 'mean'),
    avg_charges=('charges', 'mean')
)
print(region_summary)

bmi_smoker = df.groupby(['bmi_category', 'smoker'])['charges'].mean()
print(bmi_smoker)

pivot_table = pd.pivot_table(
    df,
    values='charges',
    index='sex',
    columns='smoker',
    aggfunc='mean'
)
print(pivot_table)

df['high_cost'] = np.where(df['charges'] > df['charges'].mean(), 'Yes', 'No')

high_cost_summary = df.groupby(['high_cost', 'smoker']).size()
print(high_cost_summary)

corr = df[['age', 'bmi', 'children', 'charges']].corr()
print(corr)




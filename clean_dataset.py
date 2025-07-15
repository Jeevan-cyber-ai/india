import pandas as pd

df = pd.read_csv('state wise pop.csv')


columns_to_drop = [col for col in df.columns if col.startswith('population(') and '2024' not in col]
df = df.drop(columns=columns_to_drop)

df = df.rename(columns={'population(2024)': 'Population_2024'})


df.to_csv('cleaned_pop_2024_only.csv', index=False)

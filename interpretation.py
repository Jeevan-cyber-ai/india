import pandas as pd


df = pd.read_csv("clustered_states.csv")
print(df['Cluster'].value_counts())


print(df.groupby('Cluster')[['Population_2024', 'GDP_Crore']].mean())

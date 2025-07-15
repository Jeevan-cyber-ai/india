import pandas as pd


df = pd.read_csv("states.csv")


df = df.rename(columns={
    'States/Uts': 'State',
    'population(2024)': 'Population_2024',
    'GDP': 'GDP_Lakh_Crore'
})


df = df[['State', 'Population_2024', 'GDP_Lakh_Crore']]


df['Population_2024'] = pd.to_numeric(df['Population_2024'], errors='coerce')
df['GDP_Lakh_Crore'] = pd.to_numeric(df['GDP_Lakh_Crore'], errors='coerce')


df.dropna(subset=['Population_2024', 'GDP_Lakh_Crore'], inplace=True)

df['GDP_Crore'] = df['GDP_Lakh_Crore'] * 100


df.drop(columns=['GDP_Lakh_Crore'], inplace=True)

df.to_csv("states_data.csv", index=False)


print(" Preprocessing complete. Saved as 'states_data.csv'\n")
print(df.head())

print(df)

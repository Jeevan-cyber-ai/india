import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


df = pd.read_csv("states_data.csv")


features = df[['Population_2024', 'GDP_Crore']]


scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

df.to_csv("clustered_states.csv", index=False)

print(" Clustering complete. Saved as 'clustered_states.csv'")
print(df[['State', 'Population_2024', 'GDP_Crore', 'Cluster']].head())
print(df)
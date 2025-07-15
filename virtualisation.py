import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("clustered_states.csv")
df_sorted = df.sort_values(by="GDP_Crore", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=df_sorted, x="State", y="GDP_Crore", hue="Cluster", dodge=False, palette="Set2")
plt.xticks(rotation=90)
plt.title("GDP by State (Cluster-wise)")
plt.tight_layout()
plt.savefig("gdp_barplot.png")
plt.show()




df_sorted = df.sort_values(by="Population_2024", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=df_sorted, x="State", y="Population_2024", hue="Cluster", dodge=False, palette="Set1")
plt.xticks(rotation=90)
plt.title("Population by State (Cluster-wise)")
plt.tight_layout()
plt.savefig("population_barplot.png")
plt.show()





df['Per_Capita_GDP'] = df['GDP_Crore'] / df['Population_2024']

plt.figure(figsize=(12, 6))
sns.barplot(data=df.sort_values('Per_Capita_GDP', ascending=False), 
            x='State', y='Per_Capita_GDP', hue='Cluster', dodge=False, palette="Set3")
plt.xticks(rotation=90)
plt.title("Per Capita GDP by State")
plt.tight_layout()
plt.savefig("per_capita_gdp.png")
plt.show()




# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='Population_2024',
    y='GDP_Crore',
    hue='Cluster',
    palette='Set1',
    s=100
)

# Plot formatting
plt.title("Indian States Clustering (Population vs GDP)", fontsize=14)
plt.xlabel("Population (2024)", fontsize=12)
plt.ylabel("GDP (₹ Crore)", fontsize=12)
plt.grid(True)
plt.tight_layout()

# Save and show
plt.savefig("clusters.png")
plt.show()



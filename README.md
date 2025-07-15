# 🇮🇳 Indian States Clustering (K-Means)

This project applies **Unsupervised Machine Learning** (K-Means clustering) to group Indian states into 3 clusters based on:
- `Population_2024`
- `GDP_Crore`

The goal is to identify meaningful regional patterns in economic and demographic data.

---

## 🧠 Objective

To cluster Indian states into **3 distinct groups** using **Population** and **Gross Domestic Product (GDP)** and visualize them to uncover patterns in development and resource distribution.

---

## 📁 Dataset

The dataset includes:
- Indian states/UTs
- Population projections for the year 2024
- GDP (Gross State Domestic Product in ₹ Crores)

➡️ Cleaned file used: `states_data.csv`

---

## ⚙️ Technologies Used

- Python 🐍
- pandas, matplotlib, seaborn
- scikit-learn (StandardScaler, KMeans)
- Jupyter Notebook / VS Code

---

## 📊 Steps Performed

1. **Data Cleaning & Preprocessing**
   - Removed unnecessary columns (other years, irrelevant stats)
   - Standardized GDP values
   - Selected 2 key features: `Population_2024`, `GDP_Crore`

2. **Clustering using K-Means**
   - Standardized features using `StandardScaler`
   - Used `KMeans(n_clusters=3)` to create 3 groups
   - Added cluster labels to dataset → `clustered_states.csv`

3. **Visualization**
   - Scatter plot of GDP vs Population colored by cluster
   - Optional plots: GDP per state, Per Capita GDP

---

## 🔍 Cluster Interpretation (Based on Actual Data)

| Cluster | Avg Population | Avg GDP      | Interpretation                                                  |
|---------|----------------|--------------|------------------------------------------------------------------|
| **0**   | ~1.6 Cr         | ₹395 Cr      | Small states/UTs with low population and low economic output     |
| **1**   | ~11.5 Cr        | ₹1570 Cr     | Overpopulated states with relatively low GDP (e.g., UP, Bihar)   |
| **2**   | ~8.6 Cr         | ₹2960 Cr     | Economically strong states with moderate population (e.g., TN, MH) |

---

## 📷 Visualizations

- `clusters.png` — GDP vs Population scatter plot
- `gdp_barplot.png` — GDP of states sorted by cluster
- `per_capita_gdp.png` — GDP per person (optional)

---

## 📁 Files Included

| File                        | Purpose                                    |
|-----------------------------|--------------------------------------------|
| `states_data.csv`           | Cleaned input dataset                      |
| `clustered_states.csv`      | Final dataset with cluster labels          |
| `preprocess_states_data.py` | Preprocessing script                       |
| `cluster_states.py`         | KMeans clustering script                   |
| `visualize_clusters.py`     | All plotting code                          |
| `README.md`                 | Project documentation                      |

---

## 🧠 Insights

Clustering clearly shows differences between:
- **Economically strong** but moderately populated states
- **Overburdened regions** with high population but weak GDP
- **Smaller UTs/states** with low economic and demographic weight

These clusters can help in policy making, targeted development, and identifying growth opportunities.

---

## 🤖 Prompt Used

> "Take the states of India. Group them into 3 clusters. You can decide how to cluster them. Decide the attributes you'll use to cluster them. Get the data as well. Write a piece of code to do this. If you can represent the clusters visually, even better. Also write a one pager on what you did and the approach you took and your conclusions."

---

## 👨‍💻 Author

*Project submitted by: [Your Name]*  
*Date: July 2025*

---

## ✅ Status

✔️ Completed and ready for submission/presentation!

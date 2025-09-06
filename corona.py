# corona_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
file1 = "COVID19_India_Sample_Data.xlsx"
file2 = "India_COVID19_Detailed_Data.xlsx"

df_sample = pd.read_excel(file1)
df_detailed = pd.read_excel(file2)

print("Sample Data:\n", df_sample.head())
print("\nDetailed Data:\n", df_detailed.head())

# -----------------------------
# 1. Clean Data
# -----------------------------
# Convert numeric columns to numbers (remove commas, text)
df_detailed["Value"] = df_detailed["Value"].replace({',': '', 'Over ': '', 'Approx. ': ''}, regex=True)
df_detailed["Value"] = pd.to_numeric(df_detailed["Value"], errors="coerce")

# -----------------------------
# 2. Visualization
# -----------------------------

# Pie chart of vaccinations by gender
vacc_data = df_detailed[df_detailed["India COVID-19 Data"].str.contains("Vaccinations")]
plt.figure(figsize=(6,6))
plt.pie(vacc_data["Value"], labels=vacc_data["India COVID-19 Data"], autopct="%1.1f%%", startangle=90)
plt.title("Vaccinations in India (Gender-wise)")
plt.show()

# Bar chart of major stats (Cases, Deaths, Vaccinations)
stats = df_detailed[df_detailed["India COVID-19 Data"].isin(
    ["Total Confirmed Cases", "Total Deaths", "Total Vaccinations Administered"]
)]
plt.figure(figsize=(8,6))
sns.barplot(data=stats, x="India COVID-19 Data", y="Value", palette="viridis")
plt.title("COVID-19 Summary in India")
plt.ylabel("Count")
plt.xticks(rotation=20)
plt.show()

# -----------------------------
# 3. Insights
# -----------------------------
print("\n--- Insights ---")
total_cases = stats.loc[stats["India COVID-19 Data"]=="Total Confirmed Cases","Value"].values[0]
total_deaths = stats.loc[stats["India COVID-19 Data"]=="Total Deaths","Value"].values[0]
vaccinated = stats.loc[stats["India COVID-19 Data"]=="Total Vaccinations Administered","Value"].values[0]

death_rate = (total_deaths / total_cases) * 100
print(f"Total Cases: {total_cases:,}")
print(f"Total Deaths: {total_deaths:,}")
print(f"Total Vaccinations: {vaccinated:,}")
print(f"Death Rate: {death_rate:.2f}%")

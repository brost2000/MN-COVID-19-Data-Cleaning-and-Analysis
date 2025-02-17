import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression 

# Note that population (of 7co) = 3065147 and counties = 7co of MPLS Metro Area
df = pd.read_csv(
    r"/Users/alexanderbrost/Desktop/root/py/regression_analysis_viz/respnetage_mn_clean.csv"
)
df = df.iloc[:, 0].str.split(";", expand=True)
df.columns = [
    "Season",
    "MMWR Startdate",
    "Age Group",
    "Count of Hospitalizations",
    "Pathogen",
]

# Cleaning data further (count to numeric, error > NaN) and 'Pathogen' == 'COVID-19'
df["Count of Hospitalizations"] = pd.to_numeric(
    df["Count of Hospitalizations"], errors="coerce"
)
df = df[df["Pathogen"] == "COVID-19"]
df["MMWR Startdate"] = pd.to_datetime(df["MMWR Startdate"])
df["Age Group"] = df["Age Group"].str.strip()


# Counting hospitalization by age-group
df_grouped = df.groupby("Age Group")["Count of Hospitalizations"].sum().reset_index()

# Sorting age groups
age_order = ["0-4", "5-17", "18-49", "50-64", "65"]
df_grouped["Age Group"] = pd.Categorical(
    df_grouped["Age Group"], categories=age_order, ordered=True
)

# Sorting the dataframe based on the defined order
df_grouped = df_grouped.sort_values("Age Group")

# Visualization
x = df_grouped["Age Group"]
y = df_grouped["Count of Hospitalizations"]

fig, ax = plt.subplots()
bars = ax.bar(x, y)

ax.bar_label(bars, fmt="%d", padding=3)

plt.xticks(rotation=45)
plt.xlabel("Age Group")
plt.ylabel("Total Hospitalizations")
plt.title("COVID-19 Hospitalizations by Age Group")
plt.show()

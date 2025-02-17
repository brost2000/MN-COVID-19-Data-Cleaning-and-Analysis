import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#measure hospitalizations over time

df = pd.read_csv(
    r"/Users/alexanderbrost/Desktop/root/py/regression_analysis_viz/respnetage_mn_clean.csv"
)

df = df.iloc[:, 0].str.split(";", expand = True)
df.columns = [
    "Season",
    "MMWR Startdate",
    "Age Group",
    "Count of Hospitalizations",
    "Pathogen",
]

#define our pathogen as == COVID-19 and counts to numeric

df["Count of Hospitalizations"] = pd.to_numeric(
        df["Count of Hospitalizations"], errors = "coerce"
)
df = df[df["Pathogen"] == "COVID-19"]
df["MMWR Startdate"] = pd.to_datetime(df["MMWR Startdate"])
df["Age Group"] = df["Age Group"].str.strip()


#Need to measure change over time by age group 

df_grouped = df.groupby(["MMWR Startdate", "Age Group"])["Count of Hospitalizations"].sum().reset_index()

plt.figure(figsize=(12, 6))

for age_group in df["Age Group"].unique():
    subset = df_grouped[df_grouped["Age Group"] == age_group]
    plt.plot(subset["MMWR Startdate"], subset["Count of Hospitalizations"], label=age_group)

plt.xlabel("Date")
plt.ylabel("Hospitalizations")
plt.title("COVID-19 Hospitalizations Over Time by Age Group")
plt.legend(title="Age Group")
plt.xticks(rotation=45)
plt.show()


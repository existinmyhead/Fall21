# Nitya Shanker
# October 12, 2021
# ECE 3100
# Program 2

import pandas as pd
import matplotlib.pyplot as plt
# from tabulate import tabulate

# TASK 1
# Read csv file
df = pd.read_csv("/Users/nityashanker/Downloads/Salaries.csv")

# TASK 2
print("TASK 2 - Standard deviation for all numerical columns:")
print(df[["phd", "service", "salary"]].agg(["std"]))
print()

# TASK 3
print("TASK 3 - Mean values of first 50 records in dataset")
df50 = df.head(50)
print(df50.agg(["mean"]))
print()

# TASK 4
print("TASK 4 - Basic statistics for salary column:")
print(df[["salary"]].agg(["mean", "median", "std"]))
print(df[["salary"]].agg(["mode"]))
print()

# TASK 5
print("TASK 5 - Different values in salary column:")
print(df[["salary"]].nunique())
print()

# TASK 6
print("TASK 6 - Mean salary for each professor rank:")
dfRank = df.groupby(["rank"]).mean()
print(dfRank[["salary"]])
print()

# TASK 7
print("TASK 7 - Mean salary for male and female professors:")
dfMaleFemale = df.groupby(['sex']).mean()
print(dfMaleFemale[['salary']])
print()

print("TASK 7 - Mean salary for rows that only contain female professors:")
df_f = df[ df["sex"] == "Female"]
df_m = df[ df["sex"] == "Male"]
df_Female = df_f.groupby(["sex"]).mean()
print(df_Female[["salary"]])
print()

# TASK 8
print("TASK 8 - Record of people who have the top 5 salaries:")
dfTop5 = df.sort_values(by = "salary", ascending = False)
print(dfTop5.head(5))
print()

# TASK 9
print("TASK 9 - Mean, min, and max salaries in department, discipline A, and discipline B:")
df_f = df.loc[df["sex"] == "Female", ["salary"]].agg(["mean", "max", "min"]).transpose()
df_m = df.loc[df["sex"] == "Male", ["salary"]].agg(["mean", "max", "min"]).transpose()
dfDepA = df.loc[df["discipline"] == "A", ["salary", "sex"]]
dfDepB = df.loc[df["discipline"] == "B", ["salary", "sex"]]
dfDepA_f = dfDepA[dfDepA["sex"] == "Female"].agg(["mean", "max", "min"]).transpose().iloc[[0]]
dfDepA_m = dfDepA[dfDepA["sex"] == "Male"].agg(["mean", "max", "min"]).transpose().iloc[[0]]
dfDepB_f = dfDepB[dfDepB["sex"] == "Female"].agg(["mean", "max", "min"]).transpose().iloc[[0]]
dfDepB_m = dfDepB[dfDepB["sex"] == "Male"].agg(["mean", "max", "min"]).transpose().iloc[[0]]
df9 = pd.concat([df_f, df_m, dfDepA_f, dfDepA_m, dfDepB_f, dfDepB_m])
df9.columns = ["salary_mean", "salary_max", "salary_min"]
df9.index = ["Female", "Male", "A_Female", "A_Male", "B_Female", "B_Male"]
df9 = df9.rename_axis("Sex", axis = "columns")
print(df9)
print()


# TASK 10
print("TASK 10 - Number of female and male faculty in entire department, discipline A, and discipline B:")
fTotal = df[df["sex"] == "Female"].count().iloc[0]
mTotal = df[df["sex"] == "Male"].count().iloc[0]
fATotal = df[ df["sex"] == "Female"][df["discipline"] == "A"].count().iloc[0]
fBTotal = df[ df["sex"] == "Female"][df["discipline"] == "B"].count().iloc[0]
mATotal = df[ df["sex"] == "Male"][df["discipline"] == "A"].count().iloc[0]
mBTotal = df[ df["sex"] == "Male"][df["discipline"] == "B"].count().iloc[0]
d = {"#female": [fTotal, fATotal, fBTotal], "#male": [mTotal, mATotal, mBTotal]}
df10 = pd.DataFrame(data=d,
                     index = ["Department", "A", "B"])


# TASK 11
print("TASK 11 - Graph to illustrate results from task 9:")
df_p = df9.plot.barh()
print(df_p)

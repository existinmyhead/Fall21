# Nitya Shanker
# November 2, 2021
# ECE 3100
# Program 3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import percentile

# Array to hold 5 number summary for all 6 files
arraysum = np.zeros((6,5))
print("Blank array to hold 5 number vectors")
print(arraysum)
print()

# TASK 1: Read in 6 vehicle files
for i in range (1,7):
    # j to iterate through summary array by row (vehicle file)
    j = i-1

    trip = "15minTrip" + str(i)
    dataframe = pd.read_csv("/Users/nityashanker/Downloads/"+trip+".csv",usecols=["Time", "Vehicle speed"])
    # check data being read in
    # print(dataframe)


# TASK 2: Plot the vehicle speed curve for each data file
    sns.lineplot(x="Time", y="Vehicle speed", data=dataframe)
    plt.title(trip)
    plt.xlabel("Time (ms)")
    plt.ylabel("Vehicle Speed (km/hr)")
    plt.show()


# TASK 4: Calculate the 5 number summary (min, Q1, median, Q3, max) for each data file
    # Remove NA values
    dataframe.dropna(inplace=True)

    quartiles = percentile(dataframe["Vehicle speed"], [25, 50, 75])

    print("5 number summary for "+trip+":")
    print("Min: %.3f" % dataframe["Vehicle speed"].min())
    arraysum[j][0] = dataframe["Vehicle speed"].min()

    print("Q1: %.3f" % quartiles[0])
    arraysum[j][1] = quartiles[0]

    print("Median: %.3f" % quartiles[1])
    arraysum[j][2] = quartiles[1]

    print("Q3: %.3f" % quartiles[2])
    arraysum[j][3] = quartiles[2]

    print("Max: %.3f" % dataframe["Vehicle speed"].max())
    arraysum[j][4] = dataframe["Vehicle speed"].max()
    print()


# TASK 3: Plot the boxplot of the vehicle speed for each data file
    dataframe.plot.box
    sns.boxplot(data=dataframe, x="Vehicle speed")
    plt.title(trip)
    plt.xlabel("Vehicle Speed (km/hr)")
    plt.text(x=dataframe["Vehicle speed"].min(), y=.45, s="Min", horizontalalignment="center")
    plt.text(x=quartiles[0], y=.45, s="Q1", horizontalalignment="center")
    plt.text(x=quartiles[1], y=.45, s="Median", horizontalalignment="center")
    plt.text(x=quartiles[2], y=.45, s="Q3", horizontalalignment="center")
    plt.text(x=dataframe["Vehicle speed"].max(), y=.45, s="Max", horizontalalignment="center")
    plt.show()

# TASK 5: Calculate the Euclidean distance of the 5-number vectors representing each pair of trips
print("5 Number Summary for all 6 Vehicle Files:")
print(arraysum)
print()

# Calculate Euclidean distance between all rows
print("Euclidean distance between all 6 Vehicle Files:")
for a in range (0,6):
    for b in range (a+1,6):
        euclid = np.linalg.norm(arraysum[b] - arraysum[a])
        print("dist (15minTrip" + str(a+1) + ", 15minTrip" + str(b+1) + ") = " + str(euclid))
        # print(np.linalg.norm(arraysum[b] - arraysum[a]))

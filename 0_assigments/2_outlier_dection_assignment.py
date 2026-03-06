import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# ---------------------------------------------
# 1 
data1 = np.array([8, 9, 10, 7, 9, 12, 90])

plt.figure()
plt.hist(data1,bins = 10,edgecolor = "black")
plt.title("Data for outlier detection")
# plt.show()

# ---------------------------------------------
# 2
data2 = np.array([15, 16, 14, 17, 16, 100])
mean = np.mean(data2)
std = np.std(data2)
z_scores = (data2 - mean) / std

print("Z-scores:", z_scores)
print("Outliers by Z-score (>2):", data2[np.abs(z_scores) > 2])

# ---------------------------------------------
# 2
data3 = np.array([5, 7, 6, 8, 5, 7, 45])
Q1 = np.percentile(data3,25)
Q3 = np.percentile(data3,75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outlier_IQR = [x for x in data3 if x<lower or x>upper ]

print("outliers :",outlier_IQR)
print("IQR :")

# ---------------------------------------------
# 3
data = np.array([10, 11, 12, 10, 13, 150])
mean = np.mean(data)
std = np.std(data)
z_score = (data-mean)/std

print("Z-scores",z_score)
print("Outlier by z-score ",data[np.abs(z_score) > 2])   

# ---------------------------------------------
# 4
data4 = np.array([25, 26, 24, 27, 30, 150])
Q1 = np.percentile(data4,25)
Q3 = np.percentile(data4,75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outlier_IQR = [x for x in data4 if x<lower or x>upper ]

print("outliers :",outlier_IQR)


# ---------------------------------------------
# 5
data5 = np.array([5, 6, 7, 8, 100])
Q1 = np.percentile(data5,25)
Q3 = np.percentile(data5,75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outlier_IQR = [x for x in data5 if x<lower or x>upper ]

print("outliers :",outlier_IQR)

# ---------------------------------------------
# 6

data6 = np.array([10, 12, 11, 13, 12, 200])

# using z_scores
mean = np.mean(data6)
std = np.std(data6)
z_score = (data6-mean)/std

print(z_score)
print("Outlier by z-score ",data6[np.abs(z_score) > 2])   

# using IQR
Q1 = np.percentile(data6,25)
Q3 = np.percentile(data6,75)

IQR = Q3 - Q1

lower = Q1-1.5*IQR
upper = Q1+1.5*IQR

outlier_IQR = [x for x in data6 if x<lower or x>upper]
print("ouliers :",outlier_IQR)
# ---------------------------------------------

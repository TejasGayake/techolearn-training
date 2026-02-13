# mode purpose in data science -->not working
# shape of data  

"""remove above lines after done"""


from statistics import mean ,median ,mode

# for checking mode function
from collections import Counter

import pandas as pd

import matplotlib.pyplot as plt

marks = [34,23,52,63,36,74,23,45,76,24,44,2464,84,96,25,65,34,65,87,92,23,45,73,64,24,76,24]

print("Data : ",marks)

print('------------------------------------')
# mean
avg_marks = mean(marks)
print("Mean of Data: ",avg_marks)

print('------------------------------------')

# median
median_marks = median(marks)
print("Median :",median_marks )

print('------------------------------------')

# MODE
mode_marks = mode(marks)
print("Mode :",mode_marks)

c = Counter(marks)
print(type(c))
max_freq = max(c.values())
multiple_mode = [x for x in c if c[x] == max_freq]
print("Multiple modes : ",multiple_mode)
print('------------------------------------')


"""Skewness and kurtosis"""
data = [55,60,75,63,65,70,56,80,75]
data_series = pd.Series(data)
print("skewness :",round(data_series.skew(),2)) #round used for roundoff till 2 decimals 
print("kurtosis :",data_series.kurt())

print('------------------------------------')

# plot plt.plot(avg_marks,median_marks,mode_marks)

plt.figure(figsize=(6,4))
# plt.bar(avg_marks,median_marks,mode_marks)
plt.hist(marks)
plt.xlabel("Name")
plt.ylabel("values")
plt.title("kurtosis")
# due to y axis it is vertical
# axis = x for horizontal
plt.grid(axis = "y",linestyle = '--',alpha = 0.5) #alpha -->opacity
# plt.show()



print('------------------------------------')

# hist

plt.figure()
plt.hist(marks,bins = 500,density  = True,edgecolor = "black")

plt.title("Distribution Curve")
plt.xlabel("values")
plt.ylabel("Density")
plt.show()



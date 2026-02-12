import statistics

# for checking mode function
from collections import Counter

import pandas as pd

import matplotlib.pyplot as plt
data = [3000,4500,5000,7000,6500,4000,5500]

# meann = mean(data)
# print(meann)
mean = statistics.mean(data)
print("Mean : ",mean)


# variance = sum([(x-meann)**2 for x in data])/(len(data)-1)

sample_variance = statistics.variance(data)

print("Sample Variance : ",sample_variance)

population_variance = statistics.pvariance(data)

print("Population Variance :",population_variance) 

print('--------------------------------------')

sample_std = statistics.stdev(data)
print("Sample standard deviation : ",sample_std)

population_std = statistics.pstdev(data)
print("Population standard deviation :",population_std)


print('--------------------------------------')

# range...
print("Range : ",max(data) - min(data))
# 3000 ----> 7000 === 4000/-

print('--------------------------------------')

# coeff(variance) = std/mean  {CV}
cv = sample_std/mean
print("Cofficient of Variance : ",cv) 
# generally its value is less than 1 (1-0)


print('--------------------------------------')

# scipy based on numpy
import numpy as np
from scipy import stats

# 30 minutes is Ho
# greater than 30 h1

claimed_mean = 30

sample_data = np.array([31,33,32,34,30,32,33,31,35,32])

n = len(sample_data)
print("Sample Data : ",sample_data)
print("Sample Size(n):",n)

sample_mean = np.mean(sample_data)
print("Sample Mean :",sample_mean)

# summation of square
sum_of_squre = np.sum((sample_data - sample_mean)*2)

# sample standard deviation
sample_sd = np.sqrt(sum_of_squre / (n-1))
print("Sample S.D. :",sample_sd)

# Standard error 
standard_error = sample_sd / np.sqrt(n)
print("Standard Error : ",standard_error)

# t-statistics
# provide the real claimed data
t_stats = (sample_mean - claimed_mean)
print("t-Statistics",t_stats)

# degree of freedom
df = n-1
print("Degree of freedom :",df)

# alpha (already set as 0.05) ----> 5%
alpha = 0.05

# percet point function
"""
Returns
    x : array_like
    quantile corresponding to the lower tail probability q."""
t_critical = stats.t.ppf(1- alpha,df)
print("t_critical value:",t_critical)

# hypothesis Ho accept or reject
if t_stats > t_critical:
    print("Reject Ho hypothesis")
else :
    print("Fail to reject Ho")

# ============================================
print("=================================")

print("========Confidance Interval======")

# some parameter are already calculated
margin_of_error = t_critical*standard_error

CI_Lower = sample_mean - margin_of_error
CI_Upper = sample_mean + margin_of_error

print("Margin of Error :",margin_of_error)
print("upper limit :",CI_Upper)
print("Lower limit :",CI_Lower)

# this whole function present in {scipy library}

print("==================================")
print("======using scipy lib=============")

mean = np.mean(sample_data)
sem = stats.sem(sample_data) #calculate standard error
df = len(sample_data)

confidence_interval = stats.t.interval(
    confidence = 0.95,
    df = df,
    loc = mean,
    scale = sem
)
print("95% Confidence Interval : ",confidence_interval)

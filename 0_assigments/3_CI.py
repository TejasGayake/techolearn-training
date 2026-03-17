import pandas as pd
import numpy as np
import scipy.stats as st

# Q1   ===============================================

salary = pd.Series([45000,52000,48000,50000,47000,49500,53000,46500,51000,50500])
mean_math = salary.mean()
std_dev = salary.std()

n = len(salary)

ci_low,ci_high = st.t.interval(0.95,n-1,loc = mean_math,scale = std_dev/np.sqrt(n))
print("Mean :",mean_math)
print("Standard Deviation: ",std_dev)
print("Confidence Interval : ",ci_high,ci_low)

print(f"On 95 % confidence interval, the avg salary of employee lies between {ci_low} to {ci_high}")


# Q2   ===============================================

df = pd.DataFrame({
    "Student": ['A','B','C','D','E','F','G','H'],
    "Hours": [5,7,8,6,9,4,10,6],
    "Marks":[50,65,70,60,75,45,80,55]
})

cov = np.cov(df["Hours"],df["Marks"])

cov_xy = cov[0][1]
print(cov_xy)

print(f"covariance {cov_xy} is Positive ,both hours and  marks moving same direction")

# Q3  ===============================================

corr = df['Hours'].corr(df['Marks'])
print("Correlation :",corr)

print(f"Correlation coefficient is {corr}","positive" if corr > 0 else "negative","correlation")



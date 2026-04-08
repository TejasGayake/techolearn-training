import pandas as pd
import numpy as np
import scipy.stats as st
from math import comb,exp,factorial
import matplotlib.pyplot as plt
t = '='*70
d = '-'*70

print(t)

# =================================================
# Generate Data
# =================================================
 
np.random.seed(1)
n = 40

df = pd.DataFrame({
    "Students_ID" :[f"S{i}" for i in range(101,101+n)],
    "Age" : np.random.randint(18,22,n),
    "Gender" : np.random.choice(["M","F"],n),
    "Study_Hours" : np.round(np.random.uniform(0.5,7,n),1),
    "Attendance %" : np.random.randint(50,100,n),
    "Maths" : np.random.randint(30,100,n),
    "Science" : np.random.randint(30,100,n),
    "English" : np.random.randint(30,100,n)

    })

# df.to_excel("Student_Data_raw.xlsx",index = False)

# =================================================
# Descriptive Stats
# =================================================

desc = df[["Maths","Science","English"]].describe().T
print("Descriptive Stats : \n",desc)

print(d)

desc["Mode"] = df[["Maths","Science","English"]].mode().iloc[0]
print("Descriptive Stats (+mode):\n",desc)

print(t)

# =================================================
# Probability
# =================================================

p_maths_over_60 = (df["Maths"]>60).mean()
print("Probability of Marks > 60 : ",p_maths_over_60)


print(t)

# =================================================
# Plot graph (Histogram)
# =================================================


# plt.hist(df["Maths"],bins = 10,edgecolor = "Black")
# plt.title("Maths Distribution")
# plt.show()

# =================================================
#  Probability Distributions
# =================================================

# normal Distribution
stats,p_value = st.shapiro(df["Maths"])
print("Sharpio P-value : ",p_value)

print(d)

# Binomial Distribution
p_pass = (df["Maths"] >= 40).mean()
binom_p = st.binom.pmf(3,5,p_pass)  #3 out of 5
print("Biomial Distribution: ",binom_p)

print(d)

# Poisson Distribution
absents = [2,4,3,5,1,2,4]
lam = np.mean(absents)      
poisson_p = st.poisson.pmf(3,lam)
print("Poisson Lambda: ",poisson_p)
 
print(t)

# =================================================
# Outlier Detection
# =================================================

# IQR method

def iqr_marks(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1
    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr
    return (series < lower) | (series > upper)
outliers = iqr_marks(df["Maths"])
print("Outliers in Maths :\n",df[outliers])


print(t)

# =================================================
# Sampling techniques
# =================================================

# Random Sampling
random10  = df.sample(10,random_state = 5)
print("Random Sample 10 Students :\n",random10[["Students_ID","Science","English"]])

# Sratified Sampling
stratified = df.groupby("Gender",group_keys = False).apply(lambda x: x.sample(min(5,len(x)),random_state=5)).reset_index(drop = True)
print("Stratified Sampling :\n",stratified[["Students_ID","Gender"]])


print(t)

# =================================================
# Confidence Interval
# =================================================

mean_math = df["Maths"].mean()
std_dev = df["Maths"].std()

n = len(df)

ci_low,ci_high = st.t.interval(0.95,n-1,loc = mean_math,scale = std_dev/np.sqrt(n))
print("Mean :",mean_math)
print("Confidence Interval : ",ci_high,ci_low)

print(t)

# =================================================
# Correlation
# =================================================

corr = df["Study_Hours"].corr(df["Maths"])
print("Correlation : ",corr)

print(t)

# =================================================
# Covariance
# =================================================
cov = np.cov(df["Study_Hours"],df["Maths"])
print("Covariance : ",cov)

print(d)

cov_xy = cov[0][1]
print("Covariance of XY :",cov_xy)

print(t)

# =================================================
# 
# =================================================

# write code for print 10 numbers
for i in range(10):
    print(i)
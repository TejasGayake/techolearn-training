import numpy as np
import pandas as pd
# ======================================
""" statistical method for outlier detection """

# 1. Z-Score

data = [5,6,7,8,9,19,22,1,21,26,27,34,700]
mean = np.mean(data)
std = np.std(data)

print("Mean : ",mean)
print("Standard Deviation :",std)
    #    z score
z_score = [((x-mean)/std) for x in data] #using list comprehension
outlier_z = []

# |Z| > 3 ---->outlier
for x,z in zip(data,z_score): # zip(): function()
    if abs(z) >3:
        outlier_z.append(x)

print("Z-score : ",z_score)
print("Outliers",outlier_z)


print("-------------------------------------------------")

# 2.IQR

data1 = [10,102,11,12,13,9,8,5,150]
Q1 = np.percentile(data,25)
Q3 = np.percentile(data,75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outlier_IQR = [x for x in data if x<lower or x>upper ]

print("outliers :",outlier_IQR)
print("IQR :")


# base for data cleaning and preparation

# cap 
# transformation
# imputation


print("-------------------------------------------------")

""" outlier handling """
data ={
    "Salary" : [20000,25000,30000,32000,25000,40000,45000,50000,60000,2000000]
    }
df = pd.DataFrame(data)
print("DataFrame",df)


# Capping
# >>not applicable for extreme outlier

p95 = np.percentile(df["Salary"],95) #try to take lesser values
df['Salary_Capped'] = df['Salary'].clip(upper = p95) #imp line .clip(upper = p95)
print("95th Percentile Value :",p95)
print("After Capping :",df)



"""
# with another method

data = pd.Series([25000, 28000, 30000, 32000, 35000, 1000000])

# Define caps
lower_cap = data.quantile(0.05)
upper_cap = data.quantile(0.95)

# Apply capping
capped_data = data.clip(lower=lower_cap, upper=upper_cap)

print(capped_data.tolist())
"""



print("-------------------------------------------------")
# Imputation
# using median

median  = df["Salary"].median()
df["Salary_imputed"] = df["Salary"].where(df["Salary"] < p95,median)

print("Median :",median)
print("imputed DataFrame :\n",df)


print("-------------------------------------------------")


"""  Transformation  """
# ?learn about this

# better than capping and impution
# solve the percentage finding problem from capping

df['log'] = np.log(df['Salary_imputed'])
df['sqrt'] = np.sqrt(df['Salary_imputed'])
print("Log Transformation :\n",df['log'])
print("Sqrt Transformation :\n",df['sqrt'])
print("-------------------------------------------------")

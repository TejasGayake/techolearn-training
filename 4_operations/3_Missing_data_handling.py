import numpy as np
import pandas as pd

data= {
    "Name" : ["Amit","Aman","Raj","Neha","Rahul","Sakshi"],
    "Age":[27,np.nan,34,26,np.nan,np.nan],
    "Salary":[30000,np.nan,30000,np.nan,24000,np.nan]
}
df = pd.DataFrame(data)
print(df)

#missing values in boolean
print(df.isnull()) 

# count of missing values
print(df.isnull().sum()) 
"""

# df_drop_rows = df.dropna() #by default remove rows 
print(df_drop_rows)

df_drop_col = df.dropna(axis = 1) #by default remove rows 
                            # axis =1 for remove column
print(df_drop_col)

"""
print("-------------------------------")

# fill null values with specific values (any data type int/str/float/complex)
df_const = df.fillna(0)
print(df_const)

print("--------------------------------")
"""
# age fill with average
df["Age"].fillna(df["Age"].mean(),inplace = True)
"""

"""only be perfomed on original array """

# --->below line of code doesn't works ----> if inplace is true -->>it will make changes in original file ,so not to be stored in another variable
# df_age_avg = df["Age"].fillna(df["Age"].mean(),inplace = True)

print("--------------------------------")

# forward fill
df_ffill = df.fillna(method = "ffill")

# df_ffill = df.ffill() #for forward fill
print("after forward fill\n",df_ffill)

print("--------------------------------")
""" DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.      
  df_bfill = df.fillna(method ="bfill")"""

df_bfill = df.fillna(method ="bfill")
# updated method
# df_bfill = df.bfill() #for backward fill

print("After backward fill\n",df_bfill)

"""
      Name   Age   Salary
0    Amit  27.0  30000.0
1    Aman  34.0  30000.0y
2     Raj  34.0  30000.0
3    Neha  26.0  24000.0
4   Rahul   NaN  24000.0
5  Sakshi   NaN      NaN
?due to backward fill last null values still null

--> viseversa for forward fill

"""

t = '='*70
d = '-'*70
print(t)
import pandas as pd

data = {
    "Age" :[25,40,60],
    "Salary": [30000,70000,100000],
    "Experience" : [2,10,20]
}

df = pd.DataFrame(data)
print("Original DataFrame :\n",df)

print(d)

# ==================================================
# Normalization
# ==================================================

df_norm = df.copy()
df_norm["Age"] = (df["Age"]-df["Age"].min())/(df["Age"].max()-df["Age"].min())

df_norm["Salary"] = (df["Salary"]-df["Salary"].min())/(df["Salary"].max()-df["Salary"].min())

df_norm["Experience"] = (df["Experience"]-df["Experience"].min())/(df["Experience"].max()-df["Experience"].min())

print("normalized DataFrame :\n",df_norm)

print(d)

# ==================================================
# Standardization
# ==================================================

df_std = df.copy()
df_std["Age"] = (df["Age"]-df["Age"].mean())/df["Age"].std()

df_std["Salary"] = (df["Salary"]-df["Salary"].mean())/df["Salary"].std()

df_std["Experience"] = (df["Experience"]-df["Experience"].mean())/df["Experience"].std()

print("After Standardization :\n",df_std)

print(d)

# ==============================================
# For Practice


data= {
    "Students":["A","B","C"],
    "Marks" : [90,86,76],
    "Study_Hours" : [6,4,2],
    "Attendence":[60,80,95]
}
df1 = pd.DataFrame(data)
print("Original DataFrame :\n",df1)


df1_norm = df.copy()
df1_norm["Marks"] = (df1["Marks"]-df1["Marks"].min())/(df1["Marks"].max()-df1["Marks"].min())

df1_norm["Study_Hours"] = (df1["Study_Hours"]-df1["Study_Hours"].min())/(df1["Study_Hours"].max()-df1["Study_Hours"].min())

df1_norm["Attendence"] = (df1["Attendence"]-df1["Attendence"].min())/(df1["Attendence"].max()-df1["Attendence"].min())

print("normalized DataFrame :\n",df1_norm)

print(d)

df1_std = df1.copy()
df1_std["Marks"] = (df1["Marks"]-df1["Marks"].mean())/df1["Marks"].std()

df1_std["Study_Hours"] = (df1["Study_Hours"]-df1["Study_Hours"].mean())/df1["Study_Hours"].std()

df1_std["Attendence"] = (df1["Attendence"]-df1["Attendence"].mean())/df1["Attendence"].std()

print("After Standardization :\n",df1_std)






print(t)
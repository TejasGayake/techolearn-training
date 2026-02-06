import numpy as np
import pandas as pd
import sqlite3

data= {
    "Name" : ["Amit","Aman","Raj"],
    "Age":[27,34,26],
    "Salary":[30000,30000,24000]
}
df = pd.DataFrame(data)
print(df)
print("------------------------")
df["Bonus"] = [2000,3000,4000]   #adding new column
print(df[["Salary","Bonus"]])
print("------------------------")

df["Bonus"] = df["Bonus"] +1000  #modification
print(df[["Salary","Bonus"]])
print("------------------------")

df.loc[df["Name"]=="Amit","Salary"] = 38000 #if salary mistaken it will create new column
print("Updated Salary:\n",df)
print("------------------------")
df["Tax"] = df["Salary"]*0.10
print("Tax :\n",df)

print("------------------------")
df.drop("Bonus",axis = 1,inplace=True)
print("droping 'Bonus' column:\n",df)

print("================================")

""" --------Missing Data -----"""


"""data frame"""
import numpy as np
import pandas as pd

print("-----------------------------------")

df = pd.DataFrame({
    "Name" : ["Pooja","Om","Amit"],
    "Department" : ["HR","IT","Sales"],
    "Salary" : [25000,20000,27000]
})
print("DataFrame with Dictionary :\n",df)

print("-----------------------------------")

data = [
    [1, "Neeraj", 89],
    [2,"Vinit", 67],
    [3,"Rahul",56]
]
df_list = pd.DataFrame(data,columns = ["Roll No","Name","Marks"])
print(df_list)

print("-----------------------------------")

# by adding values using arange values

arr = np.arange(1,13).reshape(3,4)   #reshape() use for 1d---->2D 
df_np = pd.DataFrame(arr,columns = ["A","B","C","D"])
print(df_np)
print("-----------------------------------")

s1 = pd.Series([101,102,103],index = ["A","B","C"])
s2 = pd.Series(["Anuj","Amman","Raj"],index = ["A","B","C"])
s3 = pd.Series(["IT","CS","HR"],index = ["A","B","C"])
data1 = {"Emp_Id" : s1,
         "Emp_Name" :s2,
         "Emp_Department":s3
}
df2 = pd.DataFrame(data1)

print("DataFrame with Series-->dictionary-->df :\n",df2)

print("-----------------------------------")
"""
# for seaborn inbuilt data frame is present
# but need to be import
# so we can use head() and tail() functions
# shape()
# bifurcation between tow values or categories

# df.object  --.>? 

"""
# ----------------------------------------------------



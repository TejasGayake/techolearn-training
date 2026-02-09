import pandas as pd

df = pd.DataFrame({
    "Emp_ID":[101,102,103,104,105],
    "Name": ["Amit","Neha","Rahul","Puja","Sakshi"],
    "Department":["IT","HR","IT","Sales","HR"],
    "Salary":[60000,50000,45000,60000,40000]
})


print(df.sort_values(by = "Salary",ascending=False))
print("-----------------------------------------")
print(df.sort_index(ascending=False))

print("-----------------------------------------")
# groupby  function
# it shows the index of values in the departmet columns with 
# >> {'HR': [1, 4], 'IT': [0, 2], 'Sales': [3]}
group = df.groupby("Department").groups
print(group)

print("-----------------------------------------")

df.groupby("Department").agg({
    "Emp_ID":"count",
    "Salary":"mean"
})
print(df.groupby)
# above line may be wrong

print("-----------------------------------------")

print(df.groupby(["Department","Name"])["Salary"].sum())

print("-----------------------------------------")
# transform dataframe without creating new column    ?something wrong with this statement
df["Avg_Dept_salary"] = df.groupby("Department")["Salary"].transform("mean")
print(df)
print("-----------------------------------------")
# merge
# 
emp = pd.DataFrame({
    "Emp_ID":[101,102,103,106],
    "Name":["Amit","Neha","Rahul","Riyya"]
})

dept = pd.DataFrame({
    "Emp_ID":[101,104,106],
    "Department":["IT","HR","Sales"]
    })

print(pd.merge(emp,dept,on = "Emp_ID",how = "inner"))
# works like intersection
# shows only common data
# similar like inner join in SQL
print("-----------------------------------------")
print(pd.merge(emp,dept,on = "Emp_ID",how = "right"))

print("-----------------------------------------")
# indexbased joining
# we also need to use index in it
print(emp.set_index("Emp_ID").join(dept.set_index("Emp_ID"),how = "left"))
print("-----------------------------------------")
df1 = pd.DataFrame({"A":[1,2]})
df2 = pd.DataFrame({"B":[3,4]})

print(pd.concat([df1,df2],ignore_index = True))

print("-----------------------------------------") 
# need to define index manually
# ===Label based indexing ====
emp = pd.DataFrame({
    "Emp_ID":[101,102,103,106],
    "Name":["Amit","Neha","Rahul","Riyya"]
},index = ["A","B","C","D"])
 
print(emp.loc["B"])

print("-----------------------------------------") 


# iloc integer based indexing
print(emp.iloc[2])

print("-----------------------------------------") 

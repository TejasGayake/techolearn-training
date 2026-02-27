# ====================================
#  Handling missing data
# ====================================
import numpy as np
import pandas as pd
data = {
    "Name" : ["Amit","Riya","Sneha","Amit","Divya"],
    "Age" : [25,None,30,25,28],
    "City" : ["Pune","Mumbai",None,"Pune","PUNE"],
    "Salary":[30000,35000,400000,53000,356000],
    "JoinDate":["2025-01-01","2025-05-05","2025-03-06","2025-07-01","Wrong_Date"]
}

df = pd.DataFrame(data)
print("DataFrame :\n",df)

# ---------------------------------------
print('='*60)

#capitalize first letter
df["City"] = df["City"].str.title() 

#fill none by mean value
df["Age"] = df["Age"].fillna(df["Age"].mean()) 

df['City'] = df['City'].fillna(df['City'].mode()[0])

df = df.drop_duplicates() #not working

df['JoinDate'] = pd.to_datetime(df["JoinDate"],errors = "coerce")

print(df.dtypes)

limit = df["Salary"].quantile(0.50) #50 percetile

df["Salary"] = df["Salary"].clip(upper=limit)
print("DataFrame :\n",df)


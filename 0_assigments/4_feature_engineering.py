# Q1===========================================
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "ID" : [1,2,3,4,5],
    "Price_lakh": [50,70,30,110,np.nan],
    "Area" : [800,1200,600,2000,850],
    "Rooms" : [2,3,1,4,2],
    "City": ["Pune","Mumbai","Nagpur","Mumbai","Pune"],
    "Built_year" : [2010,2018,2000,2022,2015],
    "Title": ["Cozy 2BHK near market","Spacious 3BHK luxury flat","Affordable small home","Luxurious 4BHK with terrace","Well maintained 2BHK"]
})

# tasks ========

# 1 data cleaning
df["Price_lakh"] = df["Price_lakh"].fillna(df["Price_lakh"].median())
print(df["Price_lakh"])

# 2 numeric feature engineering
df["Price_per_sqft"] = df["Price_lakh"]/df["Area"]
df["Area_per_room"] = df["Area"]/df["Rooms"]
df["Price_per_room"] = df["Price_lakh"]/df["Rooms"]

# 3 date/age feature
df["Age"] = 2026 - df["Built_year"]

# 4 binning
label1 = ["small","medium","large"]
df["area_bin"] = pd.cut(df["Area"],bins = [0,700,1500,9999],labels = label1) 

label2 = ["low","mid","high"]
df["price_bucket"] = pd.cut(df["Price_lakh"],bins = [0,40,80,500],labels= label2)

# 5 simple categorical Encoding
city_codes = {
    "Pune" : 1,
    "Mumbai": 2,
    "Nagpur" : 3
}
df["city_categories"] = df["City"].map(city_codes)

# 6 text features
df["title_word_count"] = df["Title"].apply(lambda x: len(x.split()))

df["contains_luxury"] = df["Title"].str.lower().apply(lambda x: 1 if ("luxury" in x or "luxurious" in x) else 0)

print("After feature enginnering Dataset 2\n",df)


# Q2===========================================

emp = pd.DataFrame({
    "emp_id":[101,102,103,104,105],
    "salary":[45000,52000,np.nan,80000,60000],
    "experience":[2,5,1,8,4],
    "department":["HR","IT","Finance","IT","HR"],
    "join_year":[2020,2017,2022,2015,2018],
    "feedback":["Good team player",
            "Excellent technical knowledge",
            "Needs improvement",
            "Very good and hard working",
            "Average performance"]
})
print(emp)

# tasks ========

# 1 missing value handling
emp["salary"] = emp["salary"].fillna(emp["salary"].mean())

# 2 numeric feature engineering
emp["salary_per_year"] = emp["salary"]/emp["experience"]
emp["experience_level"] = emp["experience"]/10
emp["experience_squared"] = emp["experience"]**2

# 3 date feature
emp["year_in_company"] = 2026 - emp["join_year"]

# 4 binning
label3 = ["junior","mid","senior"]
experience_bin = pd.cut(emp["experience"],bins = [0,2,5,99],labels = label3)

label4 = ["low","medium","high"]
salary_bucket = pd.cut(emp["salary"],bins = [0,50000,70000,10000000],labels = label4)

# 5 categorical encoding(no one-hot)
dept_codes = {
    "HR" : 1,
    "IT" : 2,
    "Finance" : 3
}
emp["dept_code"] = emp["department"].map(dept_codes)

# 6 text features
emp["feedback_word_count"] = emp["feedback"].apply(lambda x : len(x.split()))
emp["contains_good"] = emp["feedback"].str.lower().apply(lambda x : 1 if "good" in x else 0)

print("After feature enginnering Dataset 2\n",emp)
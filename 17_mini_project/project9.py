import pandas as pd
from datetime import datetime
# make sure all the arrays arrays in the data dictionary have the same length

data= {
    "Item" : ["Rice", "Wheat", "Sugar", "Milk","Curd","Soap","Shampoo","Toothpaste","Biscuits","Juice","Pulses","Oil"],
    "Category" : ["Grocery", "Grocery", "Grocery", "Dairy", "Dairy", "Cosmetics", "Cosmetics", "Bakery", "Snacks","Beverages","Grocery","Grocery"],
    "Stock": [20,5,10,100,70,170,190,50,35,250,270,160],
    "Price" : [40,42,45,70,50,25,90,150,10,10,30,20],
    # set the different expiry dates for different items,and it should be before and after of current date ,so kindly change them

    "Expiry_Date" : [datetime(2025, 1, 1), datetime(2027, 1, 1), datetime(2024, 6, 1), datetime(2028, 3, 15), datetime(2026, 1, 1), datetime(2026, 12, 1), datetime(2025, 11, 11), datetime(2029, 5, 20), datetime(2024, 9, 9), datetime(2027, 7, 4), datetime(2026, 3, 3), datetime(2026, 8, 8)]
}

df= pd.DataFrame(data)
print(df)

df["Total_Value"] = df["Stock"]*df["Price"]
print(df)

category_profit = df.groupby("Category")["Total_Value"].sum()
print(category_profit)

# try with datetime(today)

#expiry risk  detection
# df["Expiry_Risk"] = df["Expiry_Date"].apply(lambda x: "High Risk" if x < datetime(2023, 12, 31) else "Low Risk")

# try to use previous dataset
df["Expiry_Date"]= pd.to_datetime(df["Expiry_Date"])
today = pd.to_datetime("today")
df["Days_Left"] = (df["Expiry_Date"] - today).dt.days
expiry_risk = df[df["Days_Left"] <= 30]
print("Expiry Items:",expiry_risk[["Item", "Days_Left"]])

''''''''''''''''''';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;ll''''''l'o;;???????????'''
# Stocks movement
stock_summary = df[["Item", "Stock"]].sort_values(by="Stock")
print("Stock Movement : \n ",stock_summary)

# Purchase_Planning
df["Purchase_Status"] = df["Stock"].apply(lambda x:"Reorder" if x<70 else "No Purchase" if x>150 else "Maintain")
print(df)
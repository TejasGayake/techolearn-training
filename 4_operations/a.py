import numpy as np
import pandas as pd
import sqlite3

df = pd.DataFrame({
    "Students_ID": [101,102,103,104],
    "Name":["Neha","Aman","Pooja","Amol"],
    "Marks":[85,76,91,56],
    "Department":["Maths","Physics","Chemistry","Biology"]
})
print(df)

# to convert Dataframe ---> CSV
df.to_csv("Student_data.csv",index = False) #index can be modifies or changed

# convert DataFrame ---> excel
df.to_excel("Student_data_excel.xlsx",index = False) #.xlsx extensiion for excel file

# df --> json
df.to_json("Student_data_json.json",orient = "records")

conn = sqlite3.connect("Students_Data.db")
df.to_sql("Student_table",conn,if_exists = "replace",index = False)
# df.to_sql("Student_table",conn,if_exists = "replace",index = False)

print("----------------------------")
df_excel = pd.read_excel(r"G:\technolearn_training\29\02_pandas_library\Student_data_excel.xlsx")
print(df_excel)
print("-----------------------------")

# for json 
# for csvv
# fro json

df_sql = pd.read_sql("SELECT * FROM Students_table",conn)
print(df_sql)


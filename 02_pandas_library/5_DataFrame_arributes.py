import numpy as np
import pandas as pd

# dtype always object for column values

print('---------------------------------------')
df = pd.DataFrame({     
    "Name": ["Amit","Sneha","Neeraj","Pooja","Ravi","Vinit","Prachi","Sakshi"],
    "Age" : [23,25,29,21,22,26,25,24],
    "Scores":[89.4,24.6,24.5,34,64,23,46,80],
    "Department":["IT","Finance","HR","Finance","Sales","HR","IT","Sales"]
})
print("DataFrame : \n",df)
print("Shape of DataFrame :",df.shape)
print("Total Elements : ",df.size)
print("dimension:",df.ndim)  #ndim for dimension check
print("Columns : ",df.columns)
print("Values : ",df.values) #numpy array format
                             #looks like list

print('---------------------------------------')

print("first 5 rows : ",df.head()) #default 5*
print("first 6 rows : ",df.head(6)) 
# similar for tail
print("last 5 rows :",df.tail())

print('---------------------------------------')

print("Info :",df.info())

print('---------------------------------------')

print("Describe :",df.describe())






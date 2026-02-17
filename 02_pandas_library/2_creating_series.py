# series
# dataframe
"""creating series
 -normal 
 -with custom index
 -from a dictionary
 -usiing scalar value  #all values are same but different for column name

 """

import pandas as pd
import numpy as np

s = pd.Series([10,20,30])
print("Series with default Index : \n",s)

print("----------------------------------------")

s1 = pd.Series([40,50,60],index = ['a','b','c'])
print("Series with custom Index : \n",s)

# loc['a'] -->label based indexing
# iloc[0]  -->integer index based indexing

print("----------------------------------------")       

data = {"Name":"Raj",
        "Age":22,
        "Marks": 85}
s_dt = pd.Series(data)
print("Series from dictionary : \n",s_dt)

print("----------------------------------------")
s_scaler = pd.Series(10,index=["a","b","c","d"])
print("Scalar value Series :\n",s_scaler)

print("----------------------------------------")

arr = np.array([5,10,15,20,25])
s_arr = pd.Series(arr,index = ["p","q","r","s","t"])
print("Series from numpy array :\n",s_arr)

print("----------------------------------------")

"series operations"

 
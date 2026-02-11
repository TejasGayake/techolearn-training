import numpy as np
import pandas as pd

# for the work of series manipulation numpy array doensn't required
s = pd.Series([10,20,30])


s2 = pd.Series([10,20,30,40],index = ["P","Q","R","S"])
print(s2.iloc[3])
"----------------------------------------------------"

# loc label based indexing
#  iloc integer based indexing

"----------------------------------------------------"
s2 = pd.Series([10,20,30,40], index = ["P","Q","R","S"])
print(s2.iloc[1:3])

print("----------------------------")
# aggregation function

s2 = pd.Series([11,22,33])
print(s+s2)
print(s2 * 2)
print("SUM : ",s2.sum())
print("Mean : ",s2.mean())

print("----------------------------")

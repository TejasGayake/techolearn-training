# =============================\
#  Correlation **
# =============================
import numpy as np
import math

x = [10,20,30,40,50]
y = [15,25,35,45,55]

sum_x = sum(x)  #step1--> summation of x and y
sum_y = sum(y)

n = len(x)      #step2--> value of n

# ----requirements for step3
sum_x2 = 0
sum_y2 = 0
sum_xy = 0

# step 3
for i in range(n):
    sum_x2 = sum_x2 + x[i] * x[i]
    sum_y2 = sum_y2 + y[i] * y[i]
    sum_xy = sum_xy + x[i] * y[i]


# step 4
numerator = n*sum_xy - sum_x * sum_y
denominator = math.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2-sum_y**2))
#                         std of x              std of y
# step 5(correlation)

corr = numerator / denominator
print("Correlation (manual) : ",corr)

print('='*70)

# correlation uisng inbuilt function ====================================

corrleation = np.corrcoef(x,y)[0][1]
print("Correlation using corrcoef() : ",corrleation)
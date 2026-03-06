import statistics as st

# -------------------------------------------------------
# 1
sales = [5000, 5200, 5100, 4800, 5500, 5300, 4950, 5050, 5150, 5250, 5400, 4900]

mean = st.mean(sales)
median = st.median(sales)
mode = st.mode(sales)
sample_var = st.variance(sales)
population_var = st.pvariance(sales)
sample_std = st.stdev(sales)
population_std = st.pstdev(sales)

print("Mean :",mean)
print("Median :",median)
print("Mode :",mode)
print("Sample Variance :",sample_var)
print("Population Variance :",population_var)
print("Sample Standard Deviation :",sample_std)
print("Population Standard Deviation :",population_std)

# -------------------------------------------------------
# 2
saless = [5200, 5100, 5000, 5300, 5500, 5400, 5350,
          5250, 5150, 5050,950, 4900, 4800, 4750,
          4700, 4600, 4550, 4650, 4750, 4850,4950, 
          5050, 5200, 5300, 5400, 5500, 5600, 5650, 5700, 5800]

mean = st.mean(saless)
median = st.median(saless)
mode = st.mode(saless)
sample_var = st.variance(saless)
population_var = st.pvariance(saless)
sample_std = st.stdev(saless)
population_std = st.pstdev(saless)

print("Mean :",mean)
print("Median :",median)
print("Mode :",mode)
print("Sample Variance :",sample_var)
print("Population Variance :",population_var)
print("Sample Standard Deviation :",sample_std)
print("Population Standard Deviation :",population_std)






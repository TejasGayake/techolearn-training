# try all plots of matplotlib
# the purposes of all plots individually
# some dataset are present in it (.....)


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# print(sns.get_dataset_names())


data = sns.load_dataset('tips') #dataframe 
print(data)

# first 5 rows 
print(data.head())

#last 5 rows
print(data.tail())
print(data.info())   #schema structure
print(data.describe()) #stastical summary

# to calculate total counts of each day
print(data['day'].value_counts())

print(data.nunique())

# avgbill per day

avg_bill = data.groupby('day')['total_bill'].mean()
print(avg_bill)

# -----------------------------------------
#  VISUALISATION
# -----------------------------------------

# barplot
# --------
# sns.barplot(x = 'day',y = 'total_bill',data = data)
# plt.title("Avg Bill per Day")
# plt.show()

# Count plot
# ----------
# sns.countplot(x = 'day',data = data)
# plt.title("count of customers per day")
# plt.show()

# scatter plot ---> why it use
------------
sns.scatterplot(x ='total_bill',y = 'tip',data = data)
plt.title("total bill vs tips")
plt.show()

# Histogram
# ----------
# kde = kernal density estimation
# sns.histplot(data['total_bill'],bins = 10,kde = True)
# plt.title("Distribution of Total billl")
# plt.show()
 
# boxplot -->for outlier detection
# -------
# viz. market candle data
# sns.boxplot(x = 'day',y = 'total_bill',data = data,hue = 'sex')
# plt.title("Total Distribution per day by gender")
# plt.show()

# Heatmap
# -------
# corr = data.corr(numeric_only=True)
# sns.heatmap(corr,annot=True,cmap='coolwarm') #annotation
# plt.title("correlation Heatmaps")
# plt.show()

# Pairplot
# ---------
# sns.pairplot(data = data,hue ='sex')
# plt.suptitle("Pairplot of numeric values")
# plt.show()

# # line plot
flights = sns.load_dataset('flights')
# print(flights.head())
# sns.lineplot(data =flights,x ='year',y = 'passengers')
# plt.title("Passengers trends over years")
# plt.show()


# pivottable+heatmap
# pivot_table = flights.pivot(index= 'month',columns='year',values= 'passengers')
# sns.heatmap(pivot_table,cmap='YlGnBu',annot = True)
# plt.title("passenger heatmap")
# plt.show()


# # violin plot
# sns.violinplot(x = 'day',y='total_bill',data = data)
# plt.title('violin plot')
# plt.show()


# # KDE plot
# sns.kdeplot(data['total_bill'],fill = True )
# plt.show()


# ==============================
# data science related
# ==============================

# # Regression plot
# sns.regplot(x='total_bill',y = 'tip',data= data) #show scatter plot and best fit line
# plt.title("Regression Line")
# plt.show()

# for view multiple plots in one plot
# {subplot}
# plt.subplot(1,2,1)
# sns.histplot(data['total_bill'])
# # -------------------------------
# plt.subplot(1,2,2)
# sns.boxplot(x = 'day',y='total_bill',data = data)

plt.show()
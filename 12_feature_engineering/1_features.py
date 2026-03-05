import pandas as pd
import numpy as np
# ----------
t = '='*70
d = '-'*70
# -----------
print(t)
data = {
    "id" : [1,2,3,4,5],
    "price_lakh" : [50,75,30,120,None],
    "area" : [800,1200,600,2000,850],
    "bedrooms" : [2,3,1,4,2],
    "built_year" : [2010,2018,2000,2022,2015],
    "title" : ["cozy 2BHK","Spacious 3BHK in kothrud","Affordable 1BHK","Lavish 4BHK","Budget 2BHK"]

}

df = pd.DataFrame(data)
print(df)

print(t)
# =========================================
# Numerical 
# =========================================

df["price_lakh"] = df["price_lakh"].fillna(df["price_lakh"].median())


df["price_per_sq_ft"]= df["price_lakh"]/df["area"]


df['age_of_flat'] = 2026 - df["built_year"]


df['area_per_bedroom'] = df['area'] / df['bedrooms']
print(df)

print(t)

# =========================================================

label = ['very_small','small','medium','large']
df['area_bin'] = pd.cut(df['area'],bins = [0,700,1000,1500,9999],labels = label) #viz. barplot 
                                                                #end value is thresholod
                                                                #it does not consider the value > threshold
print(df)

# ---------------------------------------------------------
print(d)

df['title_word_count'] = df['title'].str.split().str.len()
print(df)
# ---------------------------------------------------------
print(d)

df['Contains_Lavish'] = df["title"].str.lower().str.contains("lavish").astype(int)
print(df)

print(t)
# =========================================================

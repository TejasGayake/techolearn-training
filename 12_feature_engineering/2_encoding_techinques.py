""""Enoding Techniques"""
# ----------
t = '='*70
d = '-'*70
# -----------

import pandas as pd

df = pd.DataFrame({
    "Gender" : ["Male","Female","Female","Male"],  #Binary Feature -->Label encoding
    "City" : ["Pune","Mumbai","Pune","Delhi"],
    "Education" : ["Graduate","Post Graduate","Graduate","PHD"]

})

print(df)

print(d)

print("Data Type -\n",df.dtypes)

print(t)
# =========================================
# Nominal Encoding techniques (Nominal Features)
# =========================================

# Label Encoding
df["Gender_Label"] = df["Gender"].map({"Male" : 0,"Female":17})
print("After( Label Encoding ) :\n",df)


print(d)
# -----------------------------------------

# One-Hot Endoding
city_encoded = pd.get_dummies(df["City"]).astype(int)
df = pd.concat([df,city_encoded],axis = 1) #join column in existing df
print("After (Onehot Encoding):\n",df)

print(t)

# =========================================
# Ordinal Encoding TEchniques (features)
# =========================================

# ordinal Encoding
education_order = {
    "Graduate" : 1,
    "Post Graduate" : 2,
    "PHD" : 3
}

df ["Eduction_Order"] = df["Education"].map(education_order)
print(df)

print(d)

# -----------------------------------------

# Frequency or count Encoding

"for vast amount of data ,for normalization"
# count_map = df['City'].value_counts(normalize = True) #Get the value in the range of o - 1

count_map = df['City'].value_counts()
df['City_Count'] = df['City'].map(count_map)

print(df)                                                                                                                            



































print(t)

# =========================================
# Ordinal Encoding TEchniques (features)
# =========================================
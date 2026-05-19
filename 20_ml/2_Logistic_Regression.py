# It is an classification algorithm


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = {
    "Study_Hours": [1,2,3,4,5,6,7,8],
    "Result": [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)
print(df)

x = df[["Study_Hours"]]
y = df[["Result"]]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.20, random_state = 50)

model = LogisticRegression()
model.fit(x_train,y_train)

y_predict = model.predict(x_test)

print("Predicted Result: ",y_predict)



print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

new_study_hours = pd.DataFrame({"Study_Hours":[6.5]})
new_predict = model.predict(new_study_hours)
print(new_predict)
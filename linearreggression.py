
import pandas as pd #read agera krne ke liye data ko
import numpy as np   #arrays qagera ke liye
import matplotlib.pyplot as plt #graph bana ne ke liye
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score   #library import kari h 


dataset= pd.read_csv("c:/Users/Hp/Desktop/mohit/Housing.csv") #data read




df =pd.DataFrame(dataset)   # to form excel sheet  like structure
x= df[['area','bedrooms','bathrooms','parking','stories']] #iske basis pe prediction hogi
y=df['price'] #output

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)  

model = LinearRegression() #model bana ne ke liye
model.fit(x_train,y_train) #train karane ke liye
y_pred=model.predict(x_test) # testing model to predict

print('Pridicted Price',y_pred)
print('Actual Price',list(y_test))


mse = mean_squared_error(y_test,y_pred) #prediction kitna galat h uske liye
rmse = np.sqrt(mse) #real unit error ke liye
r2= r2_score(y_test,y_pred) #model kitna capable h predict target variable   ke liye


print(f"Rmse:{rmse:2f}")    #readable format m print krne ke liye
print(f"R2 score:{r2:2f}")


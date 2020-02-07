import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
data = pd.read_csv('headbrain.csv')
print(data.head())

X= data['Head Size(cm^3)'].values
Y= data['Brain Weight(grams)'].values

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=1)
xmean=np.mean(X_train)
ymean=np.mean(Y_train)

n=len(X_train)

num=0
denom=0
for i in range(n):
    num+=(X_train[i]-xmean)*(Y_train[i]-ymean)
    denom+=(X_train[i]-xmean)**2
b1= num/denom
b0=ymean-(b1*xmean)
print(b0)
print(b1)

xmax= np.max(X)+100
xmin= np.min(X)-100

x=np.linspace(xmin,xmax,1000)
y=b0+b1*x

plt.plot(x,y,label="Regression")
plt.scatter(X,Y,label="Scatterplot")
plt.xlabel("Head Size")
plt.ylabel("Brain Weight")
plt.legend
plt.show()

#RMSE for training data
rmse= 0
rmse1=0
rmse2=0
for i in range(len(X_train)):
    y_pred=b0+b1*X_train[i]
    rmse1+=(Y_train[i]-y_pred)**2
rmse=np.sqrt(rmse1/len(X_train))
print(rmse)

#RMSE for testing data
for i in range(len(X_test)):
    y_pred1=b0+b1*X_test[i]
    rmse2+=(Y_test[i]-y_pred1) **2
rmse=np.sqrt(rmse2/len(X_test))
print(rmse)

#R2 for training data
tss1=0
for i in range(len(X_train)):
    tss1+=(Y_train[i]-ymean)**2
r2= 1-(rmse1/tss1)
print(r2)

#R2 for testing data
tss2=0
for i in range(len(X_test)):
    tss2+=(Y_test[i]-ymean)**2
r2= 1-(rmse2/tss2)
print(r2)

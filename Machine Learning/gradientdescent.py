import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
data = pd.read_csv('headbrain.csv')
print(data.head())

X= data['Head Size(cm^3)'].values
Y= data['Brain Weight(grams)'].values

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=1) #dividing data between train and test
xmean=np.mean(X_train)
ymean=np.mean(Y_train)

c = 0 #theta0
m = 0 #theta1

L = 0.0001  # The learning Rate
epochs = 1000  # The number of iterations 

n = float(len(X_train)) # Number of elements in X

# Performing Gradient Descent 
for i in range(epochs): 
    Y_pred = m*X_train + c  # The current predicted value of Y
    D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update theta1
    c = c - L * D_c  # Update theta0
    
print (m, c)
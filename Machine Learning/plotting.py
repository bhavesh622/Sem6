import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection
from sklearn.model_selection import train_test_split
iris=datasets.load_iris()
X= iris.data
Y= iris.target
class_names = iris.target_names  
# df=pd.DataFrame(iris.data, columns=iris.feature_names)  
# df['target']=iris.target
plt.scatter(X[:,0],X[:,1],c=y)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

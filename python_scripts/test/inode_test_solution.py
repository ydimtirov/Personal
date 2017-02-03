
# Save Model Using Pickle
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
# Fit the model on 33%
model = LogisticRegression()
model.fit(X_train, Y_train)
print model





#Solution:
    
#1) Run PCA to check if there are any redundant features

from sklearn.decomposition import PCA
pca = PCA(n_components=8)    
pca.fit(X_train)
pca.explained_variance_ratio_

#array([  8.77412069e-01,   6.96924545e-02,   2.71849862e-02,
#         1.41808367e-02,   7.73737174e-03,   3.28356805e-03,
#         5.01452059e-04,   7.26135992e-06])

#If we consider components explaining less than 5% of the variance as redundant then components 3,4,5,6,7 and 8 are redundant
#If we consider components explaining less than 1% of the variance as redundant then components 5,6,7 and 8 are redundant



#2) Save the output of the logistic regression in a CSV with two extra columns (1 prediction, 2 confidence)

#Running the model without applying PCA


model = LogisticRegression()
model.fit(X_train, Y_train)
print model

X_test1 = pandas.DataFrame(X_test)


#two extra columns are appended to the X_test dataset.
#Y_predict predicts the outcome: 0 or 1
#Y_predict_confidence predicts the probabiltiy of the predicton i.e. in case of 1 it mentions the probabiltiy of it being 1 and in case of 0 it mentions the probability of it being 0

X_test1['Y_predict']= model.predict(X_test)
X_test1['Y_predict_confidence']= model.predict_proba(X_test).max(axis=1)


#writing to csv file
import numpy
X_test2 = X_test1.values
numpy.savetxt("C:/Users/df11263/Desktop/Advanced Analytics/Logistic.csv", X_test2, delimiter=",")




#Running the model after applying PCA

#Taking only 2 components for PCA and then applying Logistic Regression

pca1 = PCA(n_components=2)    
pca1.fit(X_train)

X_train_pca = pca1.transform(X_train)
X_test_pca = pca1.transform(X_test)

model_pca = LogisticRegression()
model_pca.fit(X_train_pca, Y_train)
print model_pca

X_test1_pca = pandas.DataFrame(X_test_pca)


#two extra columns are appended to the X_test dataset.
#Y_predict predicts the outcome: 0 or 1
#Y_predict_confidence predicts the probabiltiy of the predicton i.e. in case of 1 it mentions the probabiltiy of it being 1 and in case of 0 it mentions the probability of it being 0

X_test1_pca['Y_predict']= model_pca.predict(X_test_pca)
X_test1_pca['Y_predict_confidence']= model_pca.predict_proba(X_test_pca).max(axis=1)


#writing to csv file
import numpy
X_test2_pca = X_test1_pca.values
numpy.savetxt("C:/Users/df11263/Desktop/Advanced Analytics/Logistic_pca.csv", X_test2_pca, delimiter=",")




#3) Use pickle operation to serialize the algorithms and save the serialized format to a file.


#Saving the Logistic Regression model without PCA
filename = 'C:/Users/df11263/Desktop/Advanced Analytics/Logistic.sav'
pickle.dump(model, open(filename, 'wb'))


#Saving the Logistic Regression model with PCA
filename1 = 'C:/Users/df11263/Desktop/Advanced Analytics/Logistic_pca.sav'
pickle.dump(model_pca, open(filename1, 'wb'))




#4) Start an API that will use the above file to generate predictions for "class" (input to the api will be  eg 6,148,72,35,0,33.6,0.627,50 output 1 or 0)

#First go to command prompt and run the python file named logistic_api.py which has the REST api and then run the below code

import requests
import json
url = 'http://localhost:9000/api'
data = json.dumps({'preg':6, 'plas':148, 'pres': 72, 'skin': 35, 'test':0, 'mass':33.6, 'pedi':0.627, 'age':50})
r = requests.post(url, data)
print r.json()
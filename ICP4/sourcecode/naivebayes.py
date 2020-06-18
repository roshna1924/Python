#----------- Importing dataset -----------#
import pandas as pd
glass=pd.read_csv("glass.csv")

#Preprocessing data
X = glass.drop('Type',axis=1)
Y = glass['Type']

#----------Splitting Data-----------#
# Import train_test_split function
from sklearn import model_selection

# Split dataset into training set and test set
X_train,X_test,Y_train,Y_test=model_selection.train_test_split(X,Y,test_size=0.2)

#-----------Model Generation ----------#
#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model=GaussianNB()

#Train the model using the training sets
model.fit(X_train,Y_train)

#Predict the response for test dataset
Y_pred=model.predict(X_test)

#----------Evaluating the model -------------#
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("accuracy score:",metrics.accuracy_score(Y_test,Y_pred))
print(metrics.classification_report(Y_test, Y_pred))



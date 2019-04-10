# Exercise 12: Using LDA Transformed Components in Classification Model

# Continuing from Exercise 11:

# transform the training features to the training components
X_train_LDA = model.transform(X_train) 

# transform the testing features to the testing components
X_test_LDA = model.transform(X_test) 

# create a random forest model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier() 

# fit the model on the training components
model.fit(X_train_LDA, y_train) 

# generate predictions on the testing components
predictions = model.predict(X_test_LDA) 

# generate confusion matrix
from sklearn.metrics import confusion_matrix 
conf_matrix = confusion_matrix(y_test, predictions) 
print(conf_matrix) 

# style the confusion matrix
import pandas as pd
cm = pd.DataFrame(conf_matrix)
import numpy as np
cm['Total'] = np.sum(cm, axis=1)
cm = cm.append(np.sum(cm, axis=0), ignore_index=True)
cm.columns = ['Predicted 1', 'Predicted 2', 'Predicted 3', 'Total']
cm = cm.set_index([['Actual 1', 'Actual 2', 'Actual 3', 'Total']])
print(cm)

# to get the accuracy score
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)

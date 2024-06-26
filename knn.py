#-------------------------------------------------------------------------
# AUTHOR: Md Abrar Fahim
# FILENAME: knn.py
# SPECIFICATION: description of the program
# FOR: CS 5990- Assignment #3
# TIME SPENT: 4 days
#-----------------------------------------------------------*/
            
#importing some Python libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler  
from sklearn.metrics import accuracy_score

#reading the training data
df_training = pd.read_csv('weather_training.csv')

X_training = df_training.iloc[:, 1:].values  
y_training = df_training.iloc[:, -1].values


for i in range(len(X_training)):
    if isinstance(X_training[i][0], str):
        date_str = X_training[i][0].split()[0]  
        year = int(date_str)  
        X_training[i][0] = year  
    
textual_features = ['Wind Bearing (degrees)', 'Visibility (km)']  
encoder = LabelEncoder()


textual_data = np.concatenate([X_training[:, df_training.columns.get_loc(feature)].reshape(-1, 1) for feature in textual_features], axis=1)
encoder.fit(textual_data.flatten())

for i, feature in enumerate(textual_features):
    X_training[:, df_training.columns.get_loc(feature)] = encoder.transform(X_training[:, df_training.columns.get_loc(feature)])

#scaling numerical feature
scaler = StandardScaler()
X_training[:, len(textual_features):] = scaler.fit_transform(X_training[:, len(textual_features):])

#11 classes after discretization
classes = np.array([i for i in range(-22, 40, 6)])
y_training_discretized = np.digitize(y_training, classes)

#reading the test data
df_test = pd.read_csv('weather_test.csv')
X_test = df_test.iloc[:, 1:].values  
y_test = df_test.iloc[:, -1].values

#encoding textual features in test data
for i, feature in enumerate(textual_features):
    # Filter out unseen labels in test data
    test_feature = X_test[:, df_test.columns.get_loc(feature)]
    unseen_mask = ~np.isin(test_feature, encoder.classes_)
    X_test = X_test[~unseen_mask]
    y_test = y_test[~unseen_mask]

#encoding remaining test data
for i, feature in enumerate(textual_features):
    X_test[:, df_test.columns.get_loc(feature)] = encoder.transform(X_test[:, df_test.columns.get_loc(feature)])


X_test[:, len(textual_features):] = scaler.transform(X_test[:, len(textual_features):])

y_test_discretized = np.digitize(y_test, classes)

#defining the hyperparameter values of KNN
param_grid = {
    'n_neighbors': [i for i in range(1, 20)],
    'p': [1, 2],
    'weights': ['uniform', 'distance']
}


grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid_search.fit(X_training, y_training_discretized)


predictions = grid_search.predict(X_test)
accuracy = accuracy_score(y_test_discretized, predictions)

#print
print('Highest KNN accuracy so far: {:.2f}'.format(accuracy))
print('Parameters: k = {}, p = {}, weight = {}'.format(grid_search.best_params_['n_neighbors'], grid_search.best_params_['p'], grid_search.best_params_['weights']))

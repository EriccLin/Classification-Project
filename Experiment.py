# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 00:49:35 2018

@author: linjiayuan
"""

import csv
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn import metrics

# load my dataset
feature_names = []
data = []
with open('mydata.csv', newline = '') as csvfile:
    rows = csv.reader(csvfile)
    for index, row in enumerate(rows):
        if( index == 0):
            feature_names = row[1:]
        else:
            data.append(row)

def preprocess(inputData):
    def repMarriageBacktoIndex(x):
        if x == 'marriaged':
            return 2
        elif x == 'divorced':
            return 1
        else:
            return 0
    inputData = np.array(inputData)
    X = inputData[:,:-1]
    y = inputData[:, -1]
    outX = []
    outY = []
    for row in X:
        newrow = []
        newrow.append((lambda x: 1 if x == 'female' else 0)(row[1]))
        newrow.append((lambda x: 1 if x == 'True' else 0)(row[2]))
        newrow.append((lambda x: 1 if x == 'True' else 0)(row[3]))
        newrow.append((lambda x: 1 if x == 'True' else 0)(row[4]))
        newrow.append(repMarriageBacktoIndex(row[5]))
        newrow.append(int(row[6]))
        outX.append(newrow)
    for _y in y:
        outY.append((lambda x: 1 if x == 'True' else 0)(_y))
        
    return outX, outY

def get_lineage(tree, feature_names):
     left      = tree.tree_.children_left
     right     = tree.tree_.children_right
     threshold = tree.tree_.threshold
     features  = [feature_names[i] for i in tree.tree_.feature]

     # get ids of child nodes
     idx = np.argwhere(left == -1)[:,0]     

     def recurse(left, right, child, lineage=None):          
          if lineage is None:
               lineage = [child]
          if child in left:
               parent = np.where(left == child)[0].item()
               split = 'l'
          else:
               parent = np.where(right == child)[0].item()
               split = 'r'

          lineage.append((parent, split, threshold[parent], features[parent]))

          if parent == 0:
               lineage.reverse()
               return lineage
          else:
               return recurse(left, right, parent, lineage)

     for child in idx:
          for node in recurse(left, right, child):
               print (node)

X, y = preprocess(data)
print(np.array(data).shape)

print("========Use Decision Tree Classifier==========")

train_X, test_X, train_y, test_y = train_test_split( X, y, test_size = 0.2)
 
dtc = DecisionTreeClassifier()

dtc.fit( train_X, train_y)

test_y_predicted = dtc.predict( test_X)

accuracy = metrics.accuracy_score(test_y_predicted, test_y)

print( feature_names )
get_lineage(dtc, feature_names[:-1])

print(accuracy)


print("======== Use KNN method ==========")

# choose k
n_rows = np.array(train_X).shape[0]
R = np.arange(1, round(0.2 * n_rows + 1))
accuracies = []

for i in R:
    knnc = KNeighborsClassifier(n_neighbors = i)
    knnc.fit(train_X, train_y)
    test_y_predicted = knnc.predict(test_X)
    accuracy = metrics.accuracy_score(test_y, test_y_predicted)
    accuracies.append(accuracy)

# visualize
plt.scatter(R, accuracies)
plt.show()
appr_k = accuracies.index(max(accuracies)) + 1
print("choose k = %d, and we can get better accuracy = %.2f" %(appr_k, 100*accuracies[appr_k - 1]) )


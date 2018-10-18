#!/usr/bin/env python

## PART 1
# Import dataset
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()

# Split training/test data
test_idx = [0,50,100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# Tree induction
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# Predict label for new flower
print(test_target)
print(clf.predict(test_data))

## PART 2
# Export graphviz code for visualization
with open("iris_classifier.txt", "w") as f:
    f = tree.export_graphviz(clf, out_file=f, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)
    
# Enter contents of 'iris_classifier.txt' here:
# https://dreampuf.github.io/GraphvizOnline/

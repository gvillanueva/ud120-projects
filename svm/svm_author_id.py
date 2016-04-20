#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
# Import support vector classifier
from sklearn.svm import SVC

# Create support vector classifier
clf = SVC(kernel="rbf", C=10000.0)

# Train our classifier and print how long it too to train
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"

# Make predictions using the classifier
t0 = time()
labels_pred = clf.predict(features_test)
print "prediction time:", round(time() - t0, 3), "s"
print labels_pred[10]
print labels_pred[26]
print labels_pred[50]
print sum(labels_pred)

from sklearn.metrics import accuracy_score
print accuracy_score(labels_test, labels_pred)

#########################################################



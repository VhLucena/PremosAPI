import pandas as pd
import pickle
from common.GetInputValues import GetInputValues 

def RandomForest(X):
    clf = pickle.load(open('python_models/models/RfClassifier.sav', 'rb'))
    return clf.predict(X)[0]

def SupportVectorMachine(X):
    clf = pickle.load(open('python_models/models/SvmClassifier.sav', 'rb'))
    return clf.predict(X)[0]

def Adaboost(X):
    clf = pickle.load(open('python_models/models/AdaClassifier.sav', 'rb'))
    return clf.predict(X)[0]
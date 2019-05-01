from enum import Enum
import json

class ModelTypes(Enum):
    RANDOM_FOREST = "randomforest"
    SVM = "svm"
    ADABOOST = "adaboost"
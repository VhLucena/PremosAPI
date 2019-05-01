import sys
import pandas as pd
from common.ModelTypes import ModelTypes
from common.ReadInputJSON import ReadInputJSON
from common.Encoding import Encoding
from common.IO import CreateOutput
import Models

def Main():

    if len(sys.argv) != 2:
        print('usage: [filename]')
        exit(1)
    

    filename = sys.argv[1]

    inputFile = ReadInputJSON(filename)
    inputFile = pd.DataFrame.from_dict(inputFile)

    modelType = inputFile['metadata']['algorithm']

    input_file = Encoding(inputFile)

    if (modelType == ModelTypes.RANDOM_FOREST.value):
        predictedValue = Models.RandomForest(input_file)

    elif (modelType == ModelTypes.SVM.value):
        predictedValue = Models.SupportVectorMachine(input_file)
    
    elif (modelType == ModelTypes.ADABOOST.value):
        predictedValue = Models.Adaboost(input_file)
    
    outputJson = CreateOutput(predictedValue, inputFile)

    print(outputJson, end='')


if __name__ == "__main__":
    Main()
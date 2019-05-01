import json

def CreateOutput(predictedValue, inputFile):
    result = {};

    if(predictedValue == 0):
        result['class'] = "Nao"
    else:
        result['class'] = "Sim"

    result['algorithm'] = inputFile['metadata']['algorithm']

    return json.dumps(result)
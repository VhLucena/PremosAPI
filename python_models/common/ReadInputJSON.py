import json

def ReadInputJSON(filename):
    path = 'input/' + filename
    with open(path) as json_file:
        input = json.load(json_file)
        return input
import json

def readJson(relativeFilePath):
    """Read file of type json"""
    with open (relativeFilePath, mode = 'r') as  jsonData:
        data = json.load(jsonData)
    return data


def createFile(relativePath):
    """Create specified if it does not exist"""
    with open(relativePath, 'a'): pass


def writeJson(updatedData, relativeFilePath, indentation = 0, sortKeys = False):
    """Write a data to json without erasing the existing one"""
    with open(relativeFilePath, 'w') as existingData:
        json.dump(updatedData, existingData, indent = indentation, sort_keys = sortKeys)
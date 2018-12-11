import json

CONFIG_PATH = "../config.json"

with open(CONFIG_PATH, 'r') as jsonFile:
    jsonText = jsonFile.read()
    configDict = json.loads(jsonText)
    
def getExtensions():
    return configDict["extensions"]

def getSourcePath():
    return configDict["source_path"]

def getFontColor():
    return configDict["font_color"]

def getBackgroundColor():
    return configDict["bg_color"]

def getTestMode():
    return configDict["test_mode"]
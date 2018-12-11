from util.textToPng import textToPng
from os import listdir, walk
from util import readConfig


def generateBackground(targetPath="../res/background.png"):
    sourcePath = readConfig.getSourcePath()
    if readConfig.getTestMode():
        text = textFromFile()
    else:
        text = textfromFolderRecoursive(folderPath=sourcePath)
    
    fontColor = readConfig.getFontColor()
    bgColor = readConfig.getBackgroundColor()
    
    return textToPng(text, targetPath, fontColor, bgColor, fontsize=16)
    
    
def textfromFolderRecoursive(folderPath="../"):
    subFolders = [x[0] for x in walk(folderPath)]
    
    accumulatedText = ""
    
    for subFolder in subFolders:
        accumulatedText += textFromFolder(subFolder)
        
    return accumulatedText


def textFromFolder(folderPath="./"):
    files = listdir(folderPath)
    filteredFiles = list(filter(_isExtensionAccepted, files))
    
    accumulatedText = ""
    
    for fileName in filteredFiles:
        with open(folderPath + "/" + fileName, 'r') as textFile:
            accumulatedText += "\n\n##### " + fileName + " #####\n\n"
            accumulatedText += textFile.read()
            
    return accumulatedText
    
def _isExtensionAccepted(fileName):
    extensionList = readConfig.getExtensions()
    
    for extension in extensionList:
        if extension in fileName:
            # .pyc instead of .py needs to be ignored
            if fileName.split(extension)[-1] == "":
                return True
    
    return False


def textFromFile(filePath=__file__):
    with open(filePath, 'r') as textFile:
        return textFile.read()
 
        
if __name__ == "__main__":
    
    textToPng(textFromFile(), '../test/test2.png')
    generateBackground()
    
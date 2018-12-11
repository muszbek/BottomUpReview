'''
Utility functions for calculating whether a character is standing on terrain
'''
from math import ceil
from util.textToPng import LEFT_PADDING
from game import tiles


def isOnTerrain(pos, charSize, bgMap, playerWidth):
    '''
    pos and charSize are (x, y) tuples
    '''
    if _isOnLine(pos[1], charSize[1]):
        if pos[1] <= 0:     # bottom of screen is considered as terrain
            return True
        
        line = _getLine(bgMap, pos[1], charSize[1])
        return _isThisTerrainOnLine(line, pos[0], charSize[0], playerWidth)
    else:
        return False
    
    
def _isOnLine(yCoord, charHeight):
    return yCoord % charHeight == 0


def _getLine(bgMap, yCoord, charHeight):
    '''
    map is a list of lines
    
    yCoord = i * charHeight
    return i-th element of bgMap
    '''
    
    index = yCoord / charHeight
    
    if yCoord % charHeight != 0:
        message = "y-coordinate is not on a line. This function should not have been called."
        raise NotStandingOnLineException(message)
    
    pythonIndex = index - 1
    reversedPythonIndex = -(pythonIndex + 1)    # bgMap is reversed, we need to access from the end
    
    return bgMap[int(reversedPythonIndex)]
    
    
def _isThisTerrainOnLine(line, xCoord, charWidth, playerWidth):
    '''
    line is a list of tile objects
    
    for first line:
    lefPad + i * charWidth - C = xCoord    where C < charWidth, because x is rounded up
    
    while True:
        is i-th element of line a terrain tile?
        i++
        if end of i-th tile > end of player:
            break
            
            This condition has to be checked in the beginning.
            If condition fails, it still needs to run one last time.
            Hence the decremented indexing in while the condition.
        
    '''

    playerEnd = xCoord + playerWidth
    index = ceil((xCoord - LEFT_PADDING) / charWidth)
    
    while playerEnd > (LEFT_PADDING + (index - 1) * charWidth):
        pythonIndex = index - 1 # from mathematical indexing to python indexing
        index += 1              # for next cycle
        if pythonIndex < 0:
            continue
        
        try:
            if isinstance(line[pythonIndex], tiles.Code):
                return True
        except IndexError:
            continue
    
    return False


def getLineHeightsBetweenTwoHeight(charHeight, startY, endY):
    startYInt = int(startY)
    endYInt = int(endY)
    
    checkLineHeights = []
    
    if startYInt > endYInt:
        checkHeight = int(startYInt / charHeight) * charHeight
        if checkHeight == startYInt:    # no neet to check if falling starts on a line-top
            checkHeight -= charHeight   # terrain is already checked earlier in the same game cycle
            
        while checkHeight > endYInt:
            checkLineHeights.append(checkHeight)
            checkHeight -= charHeight
                
    return checkLineHeights


class NotStandingOnLineException(Exception):
    pass
    
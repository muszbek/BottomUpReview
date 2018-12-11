import pygame
from util import readConfig
from util.fileToPng import generateBackground
from util.isTerrainLogic import isOnTerrain, getLineHeightsBetweenTwoHeight


MAP_PATH = '../res/background.png'
VERTICAL_BAND_RATIO = 0.3
HORIZONTAL_BAND_RATIO = 0.3

class Background(object):
    '''
    Coordinate system is coordinates of player on the background image,
    starting from bottom left corner
    '''
    playerSize = (0, 0)

    def __init__(self, screenSize):
        self.bgMap, self.charSize = generateBackground(MAP_PATH)
        
        self.updateScreenSize(screenSize)
        print("*** Map generated, tile size is " + str(self.charSize) + " ***")
        
        self.bgColor = pygame.Color(readConfig.getBackgroundColor())
        self.bgImage = pygame.image.load(MAP_PATH).convert()
        self.bgWidth = self.bgImage.get_width()
        self.bgHeight = self.bgImage.get_height()
        self._setLimits()
        
        self.pos = (0, 0)
        
    
    def updateScreenSize(self, screenSize):
        self.screenSize = screenSize
        
    def updatePlayerSize(self, playerSize):
        self.playerSize = playerSize
        self._setBands()
        
    def getMapSize(self):
        mapWidth = max(self.screenSize[0], self.bgWidth)
        mapHeight = self.bgHeight
        return (mapWidth, mapHeight)
    
    
    def isPlayerOnTerrain(self, playerPos):
        playerPosInt = (int(playerPos[0]), int(playerPos[1]))
        return isOnTerrain(playerPosInt, self.charSize, self.bgMap, self.playerSize[0])
    
    def detectCollision(self, playerOldPos, playerNewPos):
        potentialTerrainList = getLineHeightsBetweenTwoHeight(self.charSize[1], playerOldPos[1], playerNewPos[1])
        for height in potentialTerrainList:
            correctedNewPos = (playerNewPos[0], height)
            if self.isPlayerOnTerrain(correctedNewPos):
                return correctedNewPos
            
        return playerNewPos     # no collision
        
        
    def getPlayerScreenPos(self, playerPos):
        '''
        playerPos is lower left corner of player on bg coordinate system
        '''
        # to screen coordinate system, origo bottom left of screen, bottom left corner of player
        playerScreenX = playerPos[0] - self.pos[0]
        playerScreenY = playerPos[1] - self.pos[1]
        
        # upper left corner of player
        playerScreenY += self.playerSize[1]
        
        # origo upper left of screen
        playerScreenY = self.screenSize[1] - playerScreenY
        return (playerScreenX, playerScreenY)
    
        
    def moveBg(self, playerPos):
        bgX = self.pos[0]
        bgY = self.pos[1]
        
        if bgY + self.screenSize[1] - playerPos[1] < self.UPPER_BAND:
            bgY = playerPos[1] + self.UPPER_BAND - self.screenSize[1]
        if playerPos[1] - bgY < self.LOWER_BAND:
            bgY = playerPos[1] - self.LOWER_BAND
        if bgX + self.screenSize[0] - playerPos[0] < self.RIGHT_BAND:
            bgX = playerPos[0] + self.RIGHT_BAND - self.screenSize[0]
        if playerPos[0] - bgX < self.LEFT_BAND:
            bgX = playerPos[0] - self.LEFT_BAND
            
        self.pos = self._limitPos((bgX, bgY))
    
        
    def display(self, screen):
        inversedPos = self._inversePos(self.pos)
        screenPos = self._toScreenPos(inversedPos)
        screen.fill(self.bgColor)
        screen.blit(self.bgImage, screenPos)
        
    def _limitPos(self, pos):
        '''
        Make sure the background does not go off-screen
        '''
        x = pos[0]
        y = pos[1]
        
        if x < self.LEFT_LIMIT:
            x = self.LEFT_LIMIT
        if x > self.RIGHT_LIMIT:
            x = self.RIGHT_LIMIT
        if y < self.BOTTOM_LIMIT:
            y = self.BOTTOM_LIMIT
        if y > self.TOP_LIMIT:
            y = self.TOP_LIMIT
            
        self.pos = (x, y)
        return (x, y)
    
    def _inversePos(self, pos):
        '''
        Instead of left bottom corner cordinate of screen on the bgImage system,
        left bottom corner of bgImage on screen system
        '''
        x = pos[0]
        y = pos[1]
        
        return (-x, -y)
        
    def _toScreenPos(self, pos):
        '''
        Position reference point from bottom left to top left corner
        '''
        x = pos[0]
        y = pos[1]
        
        screenX = x
        screenY = self.screenSize[1] - self.bgHeight - y
        
        return (screenX, screenY)
    
        
    def _setLimits(self):
        '''
        Make sure the background does not go off-screen
        '''
        self.BOTTOM_LIMIT = min(self.bgHeight - self.screenSize[1], 0)
        self.TOP_LIMIT = self.bgHeight - self.screenSize[1]
        
        self.LEFT_LIMIT = 0
        self.RIGHT_LIMIT = max(self.bgWidth - self.screenSize[0], 0)
        
        print("*** Setting horizontal limits for map: " + str((self.LEFT_LIMIT, self.RIGHT_LIMIT)) + " ***")
        print("*** Setting vertical limits for map: " + str((self.BOTTOM_LIMIT, self.TOP_LIMIT)) + " ***")
        
    def _setBands(self):
        HORIZONTAL_BAND = self.screenSize[0] * HORIZONTAL_BAND_RATIO
        VERTICAL_BAND = self.screenSize[1] * VERTICAL_BAND_RATIO
        
        self.LEFT_BAND = HORIZONTAL_BAND
        self.RIGHT_BAND = HORIZONTAL_BAND + self.playerSize[0]
        
        self.LOWER_BAND = VERTICAL_BAND
        self.UPPER_BAND = VERTICAL_BAND + self.playerSize[1]
        
        
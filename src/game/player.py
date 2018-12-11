import pygame
from game.physics import MAX_SPEED_X, MAX_SPEED_Y, modifySpeedByPhysics

class Player(object):
    '''
    Coordinate system is coordinates of player on the background image,
    starting from bottom left corner
    '''
    
    PLAYER_WALK_IMG_PATH = ["../res/player1.png",
                            "../res/player2.png"]
    PLAYER_JUMP_IMG_PATH = "../res/player_jump.png"
    
    ACCELERATION_X = 0.4
    JUMP_SPEED = 10
    
    reachedTop = False      # condition for winning
    

    def __init__(self, initPos=(100, 0)):
        self._createDummyImg()
        
        self.speedX = 0
        self.speedY = 0
        self.pos = initPos
        print("*** Player generated, player size is " + str(self.size) + " ***")
    
    
    def _createDummyImg(self):
        self.playerImgWalkList = []
        for path in self.PLAYER_WALK_IMG_PATH:
            self.playerImgWalkList.append(pygame.image.load(path).convert_alpha())
        
        self.playerImgJump = pygame.image.load(self.PLAYER_JUMP_IMG_PATH).convert_alpha()
        
        self.spriteLookingLeft = False
        self.spriteInAir = False
        self.playerImage = self.playerImgWalkList[0]
        self.size = (self.playerImage.get_width(), self.playerImage.get_height())
        
        
    def display(self, screen, screenPos):
        if self.spriteInAir:
            self.playerImage = self.playerImgJump
        else:
            self.playerImage = self._chooseWalkImg()
            
        if self.spriteLookingLeft:
            self.playerImage = pygame.transform.flip(self.playerImage, True, False)
            
        screen.blit(self.playerImage, screenPos)
        
    def _chooseWalkImg(self):
        '''
        Just some random logic to iterate through walk pics based on movement.
        '''
        STEP_SIZE = 30
        index = int(self.pos[0] / STEP_SIZE) % len(self.playerImgWalkList)
        return self.playerImgWalkList[index]
        
    
    def setLimits(self, mapSize):
        self.LEFT_LIMIT = 0
        self.RIGHT_LIMIT = mapSize[0] - self.size[0]
        self.BOTTOM_LIMIT = 0
        self.TOP_LIMIT = mapSize[1]
        
        print("*** Setting horizontal limits for player: " + str((self.LEFT_LIMIT, self.RIGHT_LIMIT)) + " ***")
        print("*** Setting vertical limits for player: " + str((self.BOTTOM_LIMIT, self.TOP_LIMIT)) + " ***")
        
    def setPos(self, newPos):
        self.pos = newPos
        
    def getSize(self):
        return self.size
        
    def getPos(self):
        return self.pos
    
    def getSpeed(self):
        return (self.speedX, self.speedY)
        
        
    def moveLeft(self):
        self.speedX -= self.ACCELERATION_X
        if self.speedX < -MAX_SPEED_X:
            self.speedX = -MAX_SPEED_X
            
        self.spriteLookingLeft = True
            
    def moveRight(self):
        self.speedX += self.ACCELERATION_X
        if self.speedX > MAX_SPEED_X:
            self.speedX = MAX_SPEED_X
            
        self.spriteLookingLeft = False
            
    def moveUp(self, isOnTerrain):
        if isOnTerrain and self.speedY == 0:
            self.speedY += self.JUMP_SPEED
            self.spriteInAir = True
            
        if self.speedY > MAX_SPEED_Y:
            self.speedY = MAX_SPEED_Y
            
            
    def modifySpeedByPhysics(self, isOnTerrain):
        (self.speedX, self.speedY) = modifySpeedByPhysics(isOnTerrain, (self.speedX, self.speedY))
        if self.speedY == 0:
            self.spriteInAir = False
                
                
    def calcNewPos(self):
        x = self.pos[0] + self.speedX
        y = self.pos[1] + self.speedY
        return self._limitPos((x, y))
        
        
    def _limitPos(self, pos):
        '''
        Make sure the player does not go off-map
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
            self.reachedTop = True
            
        return (x, y)
    
    def didWinYet(self):
        return self.reachedTop
    
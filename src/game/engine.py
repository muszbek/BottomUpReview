'''
The main mechanic of the game.
'''
import pygame
from game.background import Background
from game.player import Player
from util.isTerrainLogic import _isOnLine, _getLine
from util.textToPng import _printLine
from util.readConfig import getTestMode


class GameEngine(object):

    def __init__(self, screen, screenSize):
        
        self.bg = Background(screenSize)
        self.player = Player()
        self.player.setLimits(self.bg.getMapSize())
        self.bg.updatePlayerSize(self.player.getSize())
        
        self.bg.display(screen)
        pygame.display.update()
        print("*** Screen loaded ***")
        
    
    def update(self, screen):
        '''
        1 - check where player is
        2 - listen to events
        3 - events + player loc -> player speeds
        4 - player speeds -> new player loc
        5 - player loc on bg
        6 - display
        '''
        # calculating player speed
        isPlayerOnTerrain = self.bg.isPlayerOnTerrain(self.player.getPos())
        self._listenToEvents(isPlayerOnTerrain)
        self.player.modifySpeedByPhysics(isPlayerOnTerrain)
        
        # calculating player new position, bg coordinate system
        newPlayerPos = self.player.calcNewPos()
        newPlayerPosCollided = self.bg.detectCollision(self.player.getPos(), newPlayerPos)
        self.player.setPos(newPlayerPosCollided)
        
        # display
        self.bg.moveBg(newPlayerPosCollided)
        playerScreenPos = self.bg.getPlayerScreenPos(newPlayerPosCollided)
        self.bg.display(screen)
        self.player.display(screen, playerScreenPos)
        pygame.display.update()
        
        return self.player.didWinYet()
        
    def _listenToEvents(self, isOnTerrain):
        keys = pygame.key.get_pressed() # checking pressed keys
        
        if keys[pygame.K_UP]:
            self.player.moveUp(isOnTerrain)
        if keys[pygame.K_LEFT]:
            self.player.moveLeft()
            return                  # return for dominant left moving behavior
        if keys[pygame.K_RIGHT]:
            self.player.moveRight()
        if keys[pygame.K_p]:
            if getTestMode():
                self._printStatus()
            
    def _printStatus(self):
        pos = self.player.getPos()
        print("Player pos: " + str(pos))
        mapPos = self.bg.pos
        print("Map pos: " + str(mapPos))
        
        if _isOnLine(pos[1], self.bg.charSize[1]):
            line = _getLine(self.bg.bgMap, pos[1], self.bg.charSize[1])
            _printLine(line)
        
        
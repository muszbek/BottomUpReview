'''
Main executable of the game.
'''
import pygame
from pygame.locals import *
from util.loaderImage import genLoader, genWin, genWinImg
from game.engine import GameEngine
#

SCREEN_WIDTH = 640
SCREEN_HIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HIGHT)

def launch():
    pygame.init()
    
    pygame.display.set_caption('Bottom Up Review')
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.blit(genLoader(), (0, 0))
    pygame.display.update()
    
    game = GameEngine(screen, SCREEN_SIZE)
    
    clock = pygame.time.Clock()
    didWinYet = False
    while True:
        clock.tick(50)
        
        if not didWinYet:
            didWinYet = game.update(screen)
        else:
            _displayWinScreen(screen)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            
            
def _displayWinScreen(screen):
    screen.fill(pygame.Color("#000000"))
    screen.blit(genWin(), (0, 0))
    screen.blit(genWinImg(), (350, 50))
    pygame.display.update()
    
    
if __name__ == "__main__":
    launch()
    
'''
A quick script to generate a loader image before the real background loads.
'''
import pygame
from util.textToPng import textToPng


def genLoader():
    LOADER_TEXT = "\n    Loading image resources...\n"
    targetPath = "../res/loader.png"
    
    textToPng(LOADER_TEXT, targetPath, fontColor="#FFFFFF", bgColor="#000000", fontsize=24)
    
    return pygame.image.load(targetPath).convert()


def genWin():
    WIN_TEXT = "\n\n    You win.\n\n    Press ESC to quit."
    targetPath = "../res/win.png"
    
    textToPng(WIN_TEXT, targetPath, fontColor="#FFFFFF", bgColor="#000000", fontsize=24)
    
    return pygame.image.load(targetPath).convert()
    
def genWinImg():
    WIN_IMG_PATH = "../res/player_jump.png"
    winImg = pygame.image.load(WIN_IMG_PATH).convert_alpha()
    winImg = pygame.transform.flip(winImg, True, False)
    winImg = pygame.transform.scale2x(winImg)
    
    return winImg
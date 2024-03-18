import pygame
import sys
from pygame.locals import *

WHITE = (255, 255, 255)
WINDOWTYPES = ('menu', 'game')
FPS = 60
WINDOWHEIGHT = 720
WINDOWWIDTH = 1280

BGCOLOR = WHITE

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Python Go!')
    
    list = main_menu()
    current = WINDOWTYPES[0]
    
    while True: 
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blits(list)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
    
    
    
def main_menu(): 
    objList = []
    
    fontObj = pygame.font.SysFont('BELL.TTF', 32)
    titleFontObj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 50)

    titleTextObj = titleFontObj.render('Go', True, (0,0,0), (255, 255, 0))
    titleTextRectObj = titleTextObj.get_rect()
    titleTextRectObj.topleft = ( (WINDOWWIDTH/2) - (titleTextObj.get_width()/2), 10)
    objList.append((titleTextObj, titleTextRectObj))

    startButtonObj = fontObj.render('Start', True, (0,0,0), (255,255,0))
    startButtonRectObj = startButtonObj.get_rect()
    startButtonRectObj.topleft = ( (WINDOWWIDTH/2) - (startButtonObj.get_width()/2), titleTextObj.get_height() + 10 + 50)
    objList.append((startButtonObj, startButtonRectObj))
    
    optionsButtonObj = fontObj.render('Options', True, (0,0,0), (255,255,0))
    optionsButtonRectObj = optionsButtonObj.get_rect()
    optionsButtonRectObj.topleft = ( (WINDOWWIDTH/2) - (optionsButtonObj.get_width()/2), titleTextObj.get_height() + startButtonObj.get_height() + 10 + 50 + 50)
    objList.append((optionsButtonObj, optionsButtonRectObj))
    
    return objList


# def game_menu():
#     a

# def game_piece(player_color):
#     a



if __name__ == '__main__':
    main()
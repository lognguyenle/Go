import pygame
import sys
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

FPS = 60
WINDOWHEIGHT = 720
WINDOWWIDTH = 1280

BGCOLOR = WHITE

class WindowTypes:
    one = "menu"
    two = "game"

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Python Go!')
    
    blitList = main_menu(YELLOW)
    current = WindowTypes.one
    
    while True: 
        mouseClicked = False
        
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blits(blitList)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        
        match current:
            case WindowTypes.one:
                if over_menu_button(mousex, mousey, blitList):
                    blitList = main_menu(GREEN)
                else:
                    blitList = main_menu(YELLOW)
                    ##
            # case WINDOWTYPES[1]:
            #     if over
        
        pygame.display.update()
    
def main_menu(highlight): 
    objList = []
    
    fontObj = pygame.font.SysFont('BELL.TTF', 32)
    titleFontObj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 50)

    titleTextObj = titleFontObj.render('Go', True, (0,0,0), highlight)
    titleTextRectObj = titleTextObj.get_rect()
    titleTextRectObj.topleft = ( (WINDOWWIDTH/2) - (titleTextObj.get_width()/2), WINDOWHEIGHT/3)
    objList.append((titleTextObj, titleTextRectObj))

    startButtonObj = fontObj.render('Start', True, (0,0,0), highlight)
    startButtonRectObj = startButtonObj.get_rect()
    startButtonRectObj.topleft = ( (WINDOWWIDTH/2) - (startButtonObj.get_width()/2), WINDOWHEIGHT/3 + titleTextObj.get_height() + 10 + 50)
    objList.append((startButtonObj, startButtonRectObj))
    
    optionsButtonObj = fontObj.render('Options', True, (0,0,0), highlight)
    optionsButtonRectObj = optionsButtonObj.get_rect()
    optionsButtonRectObj.x
    optionsButtonRectObj.topleft = ( (WINDOWWIDTH/2) - (optionsButtonObj.get_width()/2), WINDOWHEIGHT/3 + titleTextObj.get_height() + startButtonObj.get_height() + 10 + 50 + 50)
    objList.append((optionsButtonObj, optionsButtonRectObj))
    
    return objList

def over_menu_button(x, y, objList):
    for obj in objList:
        
        if (x >= obj[1].topleft[0]) and (x <= obj[1].topleft[0] + obj[1].width) and (y >= obj[1].topleft[1]) and (y <= obj[1].topleft[1]+(obj[1].height)):
            return True
    return False
        
        
    

# def game_menu():
#     a

# def game_piece(player_color):
#     a



if __name__ == '__main__':
    main()
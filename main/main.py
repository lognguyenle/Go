import pygame
import sys
from ui_elements import UIButton
from pygame.locals import *
import constants as const


class WindowTypes:
    one = "menu"
    two = "game"

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((const.WINDOWWIDTH, const.WINDOWHEIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Python Go!')

    buttonList = main_menu()
    current = WindowTypes.one
    blitList = []

    while True: 
        mouseClicked = False
        blitList = []
        for button in buttonList:
            blitList.append(button.getBlitObj())

        DISPLAYSURF.fill(const.WHITE)
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
                for button in buttonList:
                    if button.clicked(mousex, mousey, mouseClicked):
                        print('CLICKED')

        pygame.display.update()
    
def main_menu(): 
    objList = []
    
    fontObj = pygame.font.SysFont('BELL.TTF', 32)
    titleFontObj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 50)

    titleText = UIButton('Go', const.BLACK, const.YELLOW, titleFontObj, (const.WINDOWWIDTH/2, const.WINDOWHEIGHT/3))
    objList.append(titleText)
    
    playButton = UIButton('Play', const.BLACK, const.YELLOW, titleFontObj, (const.WINDOWWIDTH/2, titleText.buttonRectObj.bottom))
    objList.append(playButton)
    
    settingsButton = UIButton('Settings', const.BLACK, const.YELLOW, titleFontObj, (const.WINDOWWIDTH/2, playButton.buttonRectObj.bottom))
    objList.append(settingsButton)
    
    quitButton = UIButton('Quit', const.BLACK, const.YELLOW, titleFontObj, (const.WINDOWWIDTH/2, settingsButton.buttonRectObj.bottom))
    objList.append(quitButton)
    
    return objList

# def main_menu_clicked(current, objList, mousex, mousey, mouseClicked):
#     for 
        
# def game_menu():
#     a

# def game_piece(player_color):
#     a



if __name__ == '__main__':
    main()
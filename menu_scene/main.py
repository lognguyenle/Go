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

ANTIALLIASING = True

BGCOLOR = WHITE

class WindowTypes:
    one = "menu"
    two = "game"
    
class UIButton:
    def __init__(self, text, color, highlightColor, fontObj, pos):
        self.pos = pos
        self.fontObj = fontObj
        self.text = text
        self.textColor = color
        self.highlightColor = highlightColor
        self.buttonObj = self.fontObj.render(self.text, ANTIALLIASING, self.textColor, WHITE)
        self.buttonRectObj = self.buttonObj.get_rect()
        self.buttonRectObj.topleft = (pos[0], pos[1])
        
    def getBlitObj(self):
        return (self.buttonObj, self.buttonRectObj)
        
    def clicked(self, mousex, mousey, mouseClicked):
        if self.buttonRectObj.collidepoint((mousex, mousey)):
            self.buttonObj = self.fontObj.render(self.text, ANTIALLIASING, self.textColor, self.highlightColor)
            if mouseClicked:
                return True
        else: 
            self.buttonObj = self.fontObj.render(self.text, ANTIALLIASING, self.textColor, WHITE)
        return False
        
    

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

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
                for button in buttonList:
                    if button.clicked(mousex, mousey, mouseClicked):
                        print('CLICKED')

        pygame.display.update()
    
def main_menu(): 
    objList = []
    
    fontObj = pygame.font.SysFont('BELL.TTF', 32)
    titleFontObj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 50)

    titleText = UIButton('Go', BLACK, YELLOW, titleFontObj, (WINDOWWIDTH/2, WINDOWHEIGHT/3))
    objList.append(titleText)
    
    playButton = UIButton('Play', BLACK, YELLOW, titleFontObj, (WINDOWWIDTH/2, titleText.buttonRectObj.bottom))
    objList.append(playButton)
    
    settingsButton = UIButton('Settings', BLACK, YELLOW, titleFontObj, (WINDOWWIDTH/2, playButton.buttonRectObj.bottom))
    objList.append(settingsButton)
    
    quitButton = UIButton('Quit', BLACK, YELLOW, titleFontObj, (WINDOWWIDTH/2, settingsButton.buttonRectObj.bottom))
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
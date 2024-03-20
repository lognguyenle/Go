# Game lifecycle inspired from https://nerdparadise.com/programming/pygame/part7

import pygame
import sys
from ui_elements import UIButton
from pygame.locals import *
import constants as const
import main_menu as menu

class WindowTypes:
    one = "menu"
    two = "game"

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((const.WINDOWWIDTH, const.WINDOWHEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Python Go!')

    current_scene = menu.MenuScene()

    while current_scene != None: 
        pressed_keys = pygame.key.get_pressed()
        
        filtered_events = []
        for event in pygame.event.get():
            quit = False
            if event.type == QUIT:
                quit = True
            elif event.type == pygame.KEYDOWN:
                quit = (event.key == pygame.K_F4) and (pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT])
            
            if quit:
                current_scene.Terminate()
            else:
                filtered_events.append(event)
                
        current_scene.ProcessInput(filtered_events, pressed_keys)
        current_scene.Update()
        current_scene.Render(DISPLAYSURF)
        
        current_scene = current_scene.next

        pygame.display.update()
        clock.tick(const.FPS)
        
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
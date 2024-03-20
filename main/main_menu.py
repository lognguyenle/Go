import pygame
import constants as const
import ui_elements as ui
import scene
from pygame.locals import *

def main_menu(): 
    obj_list = []
    
    font_obj = pygame.font.SysFont('BELL.TTF', 32)
    title_font_obj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 50)

    title_text = ui.UIButton('Go', const.BLACK, False, None, const.WHITE, title_font_obj, (const.WINDOWWIDTH/2, const.WINDOWHEIGHT/3))
    obj_list.append(title_text)
    
    play_button = ui.UIButton('Play', const.BLACK, True, const.YELLOW, const.WHITE, title_font_obj, (const.WINDOWWIDTH/2, title_text.button_rect_obj.bottom))
    obj_list.append(play_button)
    
    settings_button = ui.UIButton('Settings', const.BLACK, True, const.YELLOW, const.WHITE, title_font_obj, (const.WINDOWWIDTH/2, play_button.button_rect_obj.bottom))
    obj_list.append(settings_button)
    
    quit_button = ui.UIButton('Quit', const.BLACK, True, const.YELLOW, const.WHITE, title_font_obj, (const.WINDOWWIDTH/2, settings_button.button_rect_obj.bottom))
    obj_list.append(quit_button)
    
    return obj_list

class MenuScene(scene.Scene):
    def __init__(self):
        self.next = self
        self.obj_list = main_menu()
        self.to_render = []
        self.mousepos = (0, 0)
    
    def ProcessInput(self, events, pressed_keys):
        mouse_clicked = False
        for event in events:
            if event.type == MOUSEMOTION:
                self.mousepos = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mousepos = event.pos
                mouse_clicked = True
        for obj in self.obj_list:
            obj.update(self.mousepos[0], self.mousepos[1], mouse_clicked)
        
    def Update(self):
        self.to_render = []
        for obj in self.obj_list:
            self.to_render.append(obj.get_blit_obj())
        
    def Render(self, screen):
        screen.blits(self.to_render)
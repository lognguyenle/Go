import pygame
import constants as const
import ui_elements as ui
import scene
import game
from pygame.locals import *

SETTINGSEVENT = pygame.event.custom_type()
MENUEVENT     = pygame.event.custom_type()
PLAYEVENT     = pygame.event.custom_type()

def main_menu(): 
    obj_list = []
    title_font_obj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 70)
    font_obj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 50)

    title_text = ui.UITextBox('Go', const.BLACK, const.WHITE, title_font_obj, (const.WINDOWWIDTH/2, const.WINDOWHEIGHT/3))
    obj_list.append(title_text)
    
    play_button = ui.UIButton('Play', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, title_text.rect.bottom), event = pygame.event.Event(PLAYEVENT, {}))
    obj_list.append(play_button)
    
    settings_button = ui.UIButton('Settings', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, play_button.rect.bottom), event = pygame.event.Event(SETTINGSEVENT, {}))
    obj_list.append(settings_button)
    
    quit_button = ui.UIButton('Quit', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, settings_button.rect.bottom), event = pygame.event.Event(pygame.QUIT, {}))
    obj_list.append(quit_button)
    
    return obj_list

def settings_menu():
    obj_list = []
    title_font_obj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 70)
    font_obj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 50)
    
    settings_title_text = ui.UITextBox('Settings', const.BLACK, const.WHITE, title_font_obj, (const.WINDOWWIDTH/2, const.WINDOWHEIGHT/3))
    obj_list.append(settings_title_text)
    
    settings_button = ui.UIButton('Example Setting', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, settings_title_text.rect.bottom), None)
    obj_list.append(settings_button)
    
    back_button = ui.UIButton('Back', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, settings_button.rect.bottom), event = pygame.event.Event(MENUEVENT, {}))
    obj_list.append(back_button)
    
    return obj_list

class MenuScene(scene.BareScene):
    def __init__(self):
        self.next = self
        self.obj_list = main_menu()
        self.to_render = []
        self.mousepos = (0, 0)
        self.bgupdate = True
    
    def ProcessInput(self, events, pressed_keys):
        mouse_clicked = False
        for event in events:
            if event.type == MOUSEMOTION:
                self.mousepos = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mousepos = event.pos
                mouse_clicked = True
            if event.type == SETTINGSEVENT:
                self.SwitchToScene(SettingsScene())
            if event.type == PLAYEVENT:
                self.SwitchToScene(game.GameScene())
        for obj in self.obj_list:
            obj.update(self.mousepos[0], self.mousepos[1], mouse_clicked)
        
class SettingsScene(scene.BareScene):
    def __init__(self):
        self.next = self
        self.obj_list = settings_menu()
        self.to_render = []
        self.mousepos = (0, 0)
        self.bgupdate = True
        
    def ProcessInput(self, events, pressed_keys):
        mouse_clicked = False
        for event in events:
            if event.type == MOUSEMOTION:
                self.mousepos = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mousepos = event.pos
                mouse_clicked = True
            if event.type == MENUEVENT:
                self.SwitchToScene(MenuScene())
        for obj in self.obj_list:
            obj.update(self.mousepos[0], self.mousepos[1], mouse_clicked)
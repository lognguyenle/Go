import pygame
import constants as const
import ui_elements as ui
import scene
from pygame.locals import *

SETTINGSEVENT = pygame.event.custom_type()
MENUEVENT = pygame.event.custom_type()

class QuitButton(ui.UIButton):
    def do(self):
        event = pygame.event.Event(pygame.QUIT, {})
        pygame.event.post(event)
        
class SettingsButton(ui.UIButton):
    def do(self):
        event = pygame.event.Event(SETTINGSEVENT, {})
        pygame.event.post(event)
        
class MenuButton(ui.UIButton):
    def do(self):
        event = pygame.event.Event(MENUEVENT, {})
        pygame.event.post(event)
        


def main_menu(): 
    obj_list = []
    title_font_obj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 70)
    font_obj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 50)

    title_text = ui.UITextBox('Go', const.BLACK, const.WHITE, title_font_obj, (const.WINDOWWIDTH/2, const.WINDOWHEIGHT/3))
    obj_list.append(title_text)
    
    play_button = ui.UIButton('Play', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, title_text.rect.bottom))
    obj_list.append(play_button)
    
    settings_button = SettingsButton('Settings', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, play_button.rect.bottom))
    obj_list.append(settings_button)
    
    quit_button = QuitButton('Quit', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, settings_button.rect.bottom))
    obj_list.append(quit_button)
    
    return obj_list

def settings_menu():
    obj_list = []
    title_font_obj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 70)
    font_obj = pygame.font.Font('Ojuju-VariableFont_wght.ttf', 50)
    
    settings_title_text = ui.UITextBox('Settings', const.BLACK, const.WHITE, title_font_obj, (const.WINDOWWIDTH/2, const.WINDOWHEIGHT/3))
    obj_list.append(settings_title_text)
    
    settings_button = ui.UIButton('Example Setting', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, settings_title_text.rect.bottom))
    obj_list.append(settings_button)
    
    back_button = MenuButton('Back', const.BLACK, True, const.YELLOW, const.WHITE, font_obj, (const.WINDOWWIDTH/2, settings_button.rect.bottom))
    obj_list.append(back_button)
    
    return obj_list

class MenuScene(scene.Scene):
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
        for obj in self.obj_list:
            obj.update(self.mousepos[0], self.mousepos[1], mouse_clicked)
        
    def Update(self):
        self.to_render = []
        for obj in self.obj_list:
            self.to_render.append(obj.get_blit_obj())
        
    def Render(self, screen):
        if self.bgupdate:
            screen.fill(const.BGCOLOR)
        screen.blits(self.to_render)
        
class SettingsScene(MenuScene):
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
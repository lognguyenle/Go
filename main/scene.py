#Referenced from https://nerdparadise.com/programming/pygame/part7

from typing import List
import constants as const
import main_menu as menu
import game
from pygame.locals import *
import pygame
import ui_elements

class Scene:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events):
        print("Unfinished Scene")
        
    def Update(self):
        print("Unfinished Scene")
        
    def Render(self, screen):
        print("Unfinished Scene")
    
    def SwitchToScene(self, next_scene):
        self.next = next_scene
        
    def Terminate(self):
        self.SwitchToScene(None)
        
class BareScene(Scene):
    def __init__(self):
        self.next = self
        self.obj_list = []
        self.to_render = []
        self.mousepos = (0, 0)
        self.bgupdate = True
    
    def Update(self):
        self.to_render = []
        for obj in self.obj_list:
            self.to_render.append(obj.get_blit_obj())
        
    def Render(self, screen):
        if self.bgupdate:
            screen.fill(const.BGCOLOR)
        screen.blits(self.to_render)
        
class MenuScene(BareScene):
    def __init__(self):
        super().__init__()
        self.obj_list = menu.main_menu()
    
    def ProcessInput(self, events, pressed_keys):
        mouse_clicked = False
        for event in events:
            if event.type == MOUSEMOTION:
                self.mousepos = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mousepos = event.pos
                mouse_clicked = True
            if event.type == menu.SETTINGSEVENT:
                self.SwitchToScene(SettingsScene())
            if event.type == menu.PLAYEVENT:
                self.SwitchToScene(GameScene())
        for obj in self.obj_list:
            obj.update(self.mousepos[0], self.mousepos[1], mouse_clicked)
        
class SettingsScene(BareScene):
    def __init__(self):
        super().__init__()
        self.obj_list = menu.settings_menu()
        
    def ProcessInput(self, events: List[pygame.event.Event], pressed_keys):
        mouse_clicked = False
        for event in events:
            if event.type == MOUSEMOTION:
                self.mousepos = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mousepos = event.pos
                mouse_clicked = True
            if event.type == menu.MENUEVENT:
                self.SwitchToScene(MenuScene())
        for obj in self.obj_list:
            obj.update(self.mousepos[0], self.mousepos[1], mouse_clicked)
            
class GameScene(BareScene):
    def __init__(self):
        super().__init__()
        self.obj_list = game.game_objs()
        self.escape_menu = False
        self.escape_menu_obj = []
    
    def ProcessInput(self, events, pressed_keys):
        mouse_clicked = False
        event: pygame.event.Event
        gameboard:ui_elements.GameBoard = self.obj_list[0]
        playertext:ui_elements.UITextBox = self.obj_list[1]
        for event in events:
            if event.type == MOUSEMOTION:
                self.mousepos = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mousepos = event.pos
                mouse_clicked = True
            if event.type == game.PASS:
                gameboard.board_data.pass_turn()
                playertext.updatetext("Turn: " + gameboard.get_current_player())
            if event.type == game.BOARDUPDATE:
                playertext.updatetext("Turn: " + gameboard.get_current_player())
            if pressed_keys[pygame.K_ESCAPE]:
                for obj in game.escape_menu():
                    self.escape_menu_obj.append(obj)
        if self.escape_menu is False:
            for obj in self.obj_list:
                obj.update(self.mousepos[0], self.mousepos[1], mouse_clicked)
        else:
            for obj in self.escape_menu_obj:
                obj.update(self.mousepos[0], self.mousepos[1], mouse_clicked)
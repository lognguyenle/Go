import pygame
import constants as const
import ui_elements as ui
import scene
from pygame.locals import *

def game_objs():
    obj_list = []
    
    game_board = ui.GameBoard(const.BOARDCOLORDEF, 19, const.BLACK, (const.WINDOWHEIGHT/20,const.WINDOWHEIGHT/20), (const.WINDOWHEIGHT*18/20,const.WINDOWHEIGHT*18/20))
    obj_list.append(game_board)
    
    return obj_list

def boardObject():
    pass

class GameScene(scene.BareScene):
    def __init__(self):
        self.next = self
        self.obj_list = game_objs()
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
        for obj in self.obj_list:
            obj.update(self.mousepos[0], self.mousepos[1], mouse_clicked)
    
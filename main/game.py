import constants as const
import ui_elements as ui
from pygame.locals import *
import pygame

ESCAPEMENU = pygame.event.custom_type()

def game_objs():
    obj_list = []
    
    game_board = ui.GameBoard(const.BOARDCOLORDEF, 9, const.BLACK, (const.WINDOWHEIGHT/20,const.WINDOWHEIGHT/20), (const.WINDOWHEIGHT*18/20,const.WINDOWHEIGHT*18/20))
    obj_list.append(game_board)
    
    return obj_list

def escape_menu():
    obj_list = []
    
    
    
    return obj_list

class GameTracker:
    def __init__(self, size):
        self.current = const.PLAYERS[1]
        self.board = [[0 for i in range(size)] for j in range(size)]
    


    
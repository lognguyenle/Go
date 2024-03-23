import constants as const
import ui_elements as ui
from pygame.locals import *

def game_objs():
    obj_list = []
    
    game_board = ui.GameBoard(const.BOARDCOLORDEF, 19, const.BLACK, (const.WINDOWHEIGHT/20,const.WINDOWHEIGHT/20), (const.WINDOWHEIGHT*18/20,const.WINDOWHEIGHT*18/20))
    obj_list.append(game_board)
    
    return obj_list

def boardObject():
    pass

class GameTracker:
    def __init__(self, size):
        self.current = const.PLAYERS[1]
        self.board = [[0 for i in range(size)] for j in range(size)]
    


    
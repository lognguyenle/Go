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
        self.size = size
        self.current = const.PLAYERS[1]
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        
    def update_board(self, pos):
        if check_liberties(self, pos):
            pass
        
    def check_liberties(self, pos):
        liberty = 0
        if pos[0] > 0 and pos[0] < 18:
            if pos[1] > 0 and pos[1] < 18:
                if self.board[pos[0]][pos[1]+1] == 0:
                    liberty += 1
                if self.board[pos[0]][pos[1]-1] == 0:
                    liberty += 1
                if self.board[pos[0]+1][pos[1]] == 0:
                    liberty += 1
                if self.board[pos[0]-1][pos[1]] == 0:
                    liberty += 1
                if liberty < 4:
                    return False
            
        
            
    


    
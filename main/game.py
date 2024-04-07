import constants as const
import ui_elements as ui
from pygame.locals import *
import pygame

ESCAPEMENU = pygame.event.custom_type()

def game_objs():
    obj_list = []
    
    game_board = ui.GameBoard(const.BOARDCOLORDEF, 7, const.BLACK, (const.WINDOWHEIGHT/20,const.WINDOWHEIGHT/20), (const.WINDOWHEIGHT*18/20,const.WINDOWHEIGHT*18/20))
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
        self.corners = [[0, 0], [0, size], [size, 0], [size, size]]
        
    # Fix so board updates pieces placed in eyes 
    def update_board(self, pos):
        curr_color = self.board[pos[0]][pos[1]]
        find_color = 0
        if curr_color == 1:
            find_color = 2
        else:
            find_color = 1
        adj_pos_list = self.find_adj(pos, find_color)
        flip_parts_list = self.check_liberties(adj_pos_list, find_color)
        for posdata in flip_parts_list:
            self.board[posdata[0]][posdata[1]] = 0
        
    def find_adj(self, pos, find_color:int):
        ret_list = []
        if pos[0] > 0: 
            if self.board[pos[0]-1][pos[1]] == find_color:
                ret_list.append((pos[0]-1, pos[1]))
        if pos[0] < self.size-1:
            if self.board[pos[0]+1][pos[1]] == find_color:
                ret_list.append((pos[0]+1, pos[1]))
        if pos[1] > 0:
            if self.board[pos[0]][pos[1]-1] == find_color:
                ret_list.append((pos[0], pos[1]-1))
        if pos[1] < self.size-1:
            if self.board[pos[0]][pos[1]+1] == find_color:
                ret_list.append((pos[0], pos[1]+1))
        return ret_list
    
    def check_liberties(self, pos_list:list, find_color:int):
        ret_list = []
        liberties = 0
        for pos in pos_list:
            liberties = GameTracker.recur_check_liberties(self.board, pos, [], ret_list, find_color, self.size)
        if liberties == 0:
            return ret_list
        return []
    
    def recur_check_liberties(board, pos, checked_list:list, ret_list:list, find_color:int, size:int):
        liberties = 0
        if pos[0] > 0 and not checked_list.__contains__((pos[0]-1,pos[1])):
            curr_color = board[pos[0]-1][pos[1]]
            if curr_color == find_color:
                ret_list.append((pos[0]-1, pos[1]))
                checked_list.append((pos[0]-1, pos[1]))
                liberties = liberties + GameTracker.recur_check_liberties(board, (pos[0]-1, pos[1]), checked_list, ret_list, find_color, size)
            elif curr_color == 0: 
                return 1
        if pos[0] < size-1 and not checked_list.__contains__((pos[0]+1,pos[1])):
            curr_color = board[pos[0]+1][pos[1]]
            if curr_color == find_color:
                ret_list.append((pos[0]+1, pos[1]))
                checked_list.append((pos[0]+1, pos[1]))
                liberties = liberties + GameTracker.recur_check_liberties(board, (pos[0]+1, pos[1]), checked_list, ret_list, find_color, size)
            elif curr_color == 0: 
                return 1
        if pos[1] > 0 and not checked_list.__contains__((pos[0],pos[1]-1)):
            curr_color = board[pos[0]][pos[1]-1]
            if curr_color == find_color:
                ret_list.append((pos[0], pos[1]-1))
                checked_list.append((pos[0], pos[1]-1))
                liberties = liberties + GameTracker.recur_check_liberties(board, (pos[0], pos[1]-1), checked_list, ret_list, find_color, size)
            elif curr_color == 0: 
                return 1
        if pos[1] < size-1 and not checked_list.__contains__((pos[0],pos[1]+1)):
            curr_color = board[pos[0]][pos[1]+1]
            if curr_color == find_color:
                ret_list.append((pos[0], pos[1]+1))
                checked_list.append((pos[0], pos[1]+1))
                liberties = liberties + GameTracker.recur_check_liberties(board, (pos[0], pos[1]+1), checked_list, ret_list, find_color, size)
            elif curr_color == 0: 
                return 1
        if liberties == 0:
                ret_list.append((pos[0], pos[1]))
        return liberties
from constants import ANTIALLIASING
import constants as const
import pygame
from pygame import gfxdraw
import numpy
import game

def circle_draw(surface, x, y, width, color):
    gfxdraw.aacircle(surface, x, y, width, color)
    gfxdraw.filled_circle(surface, x, y, width, color)

class UITextBox:
    def __init__(self, text, color, bg_color, font_obj, pos):
        self.pos = pos
        self.font_obj = font_obj
        self.text = text
        self.text_color = color
        self.bg_color = bg_color
        self.surface = self.font_obj.render(self.text, ANTIALLIASING, self.text_color, self.bg_color)
        self.rect = self.surface.get_rect()
        self.rect.topleft = (pos[0], pos[1])
        self.changed = False
        
    def get_blit_obj(self):
        return (self.surface, self.rect)
    
    def update(self, mouse_x, mouse_y, mouse_clicked):
        pass

class UIButton(UITextBox):
    def __init__(self, text, color, highlight, highlight_color, bg_color, font_obj, pos, event):
        super().__init__(text, color, bg_color, font_obj, pos)
        self.highlight_effect = highlight
        self.highlight_color = highlight_color
        self.event = event
        
    def clicked(self, mouse_x, mouse_y, mouse_clicked):
        if self.rect.collidepoint((mouse_x, mouse_y)):
            if self.highlight_effect:
                    if self.changed == False:
                        self.surface = self.font_obj.render(self.text, ANTIALLIASING, self.text_color, self.highlight_color)
                        self.changed = True
            return mouse_clicked
        else:
            if self.changed:
                self.surface = self.font_obj.render(self.text, ANTIALLIASING, self.text_color, self.bg_color)
                self.changed = False
        return False
    
    def update(self, mouse_x, mouse_y, mouse_clicked):
        if self.clicked(mouse_x, mouse_y, mouse_clicked):
            self.do()
    
    def do(self):
        if self.event != None:
            pygame.event.post(self.event)
        pass

class Place:
    def __init__(self, color, coordinate, width, margin):
        self.color = color
        self.width = width
        self.margin = margin
        self.set_coordinate(coordinate)
        self.drawn = False
        self.placed = False
        self.captured = False
    
    def set_coordinate(self, coordinate):
        self.coordinate = coordinate
        self.rect = pygame.Rect(0, 0, self.width*2, self.width*2)
        self.rect.center = (self.coordinate[0]+self.margin, self.coordinate[1]+self.margin)

# Gameboard class that contains the ui and logic
class GameBoard:
    def __init__(self, color, lines, linecolor, pos, width_height):
        self.board_data = game.GameTracker(lines)
        self.color = color
        self.linecolor = linecolor
        self.lines = lines
        self.width_height = width_height
        self.surface = pygame.Surface(width_height)
        self.margin = round(width_height[0]/(self.lines+5))
        self.inner = round((width_height[0] - 2*self.margin)/(self.lines-1))
        self.genboard()
        self.board = numpy.ndarray(shape = (self.lines, self.lines), dtype = numpy.object_)
        for i in range(lines):
            for y in range(lines):
                self.board[i, y] = Place(0, (0,0), round(self.inner/2.125), const.WINDOWHEIGHT/20)
                self.board[i, y].set_coordinate((self.margin + self.inner*i, self.margin+self.inner*y))
        self.rect = self.surface.get_rect()
        self.rect.topleft = pos
        self.pos = pos
        self.changed = False
    
    def update(self, mouse_x, mouse_y, mouse_clicked):
        self.clicked(mouse_x, mouse_y, mouse_clicked)
    
    def flippiece(x, y):
        pass
    
    def genboard(self):
        self.surface.fill(self.color)
        for i in range(self.lines):
            x = self.margin + self.inner*i
            y = self.margin
            y_end = self.width_height[0]-self.margin
            pygame.draw.line(self.surface, self.linecolor, (x, y), (x, y_end), 1)
            pygame.draw.line(self.surface, self.linecolor, (y, x), (y_end, x), 1)
    
    def clicked(self, mouse_x, mouse_y, mouse_clicked):
        self.genboard()
        for i in range(self.lines):
            for y in range(self.lines):
                current = self.board[i, y]
                # Add rule where you cannot place a piece on a spot that was captured last turn
                if self.board_data.board[i][y] == 0:
                    current.placed = False
                if (mouse_clicked is True and current.rect.collidepoint(mouse_x, mouse_y)) or current.placed is True:
                    if current.placed is False and current.captured is False:
                        if self.board_data.current is const.PLAYERS[1]:
                            self.board_data.current = const.PLAYERS[0]
                            self.board_data.board[i][y] = 1
                        else:
                            self.board_data.current = const.PLAYERS[1]
                            self.board_data.board[i][y] = 2
                        self.board_data.update_board((i,y))
                    if self.board_data.board[i][y] == 1:
                        circle_draw(self.surface, self.board[i, y].coordinate[0], self.board[i, y].coordinate[1], current.width, const.BLACK)
                    elif self.board_data.board[i][y] == 2:
                        circle_draw(self.surface, self.board[i, y].coordinate[0], self.board[i, y].coordinate[1], current.width, const.WHITE)
                    current.placed = True
                elif current.rect.collidepoint(mouse_x, mouse_y) and current.captured is False:
                    if self.board_data.current is const.PLAYERS[0]:
                        circle_draw(self.surface, self.board[i, y].coordinate[0], self.board[i, y].coordinate[1], current.width, const.WHITETRANSPARENT)
                    else:
                        circle_draw(self.surface, self.board[i, y].coordinate[0], self.board[i, y].coordinate[1], current.width, const.BLACKTRANSPARENT)
                        
    def get_blit_obj(self):
        return (self.surface, self.rect)
    
class EscapeMenu:
    def __init__(self, width_height):
        self.width_height = width_height
        
    
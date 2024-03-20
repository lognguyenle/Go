from constants import ANTIALLIASING

class UIButton:
    def __init__(self, text, color, highlight, highlight_color, bg_color, font_obj, pos):
        self.pos = pos
        self.font_obj = font_obj
        self.text = text
        self.text_color = color
        self.highlight_effect = highlight
        self.highlight_color = highlight_color
        self.bg_color = bg_color
        self.button_obj = self.font_obj.render(self.text, ANTIALLIASING, self.text_color, self.bg_color)
        self.button_rect_obj = self.button_obj.get_rect()
        self.button_rect_obj.topleft = (pos[0], pos[1])
        self.changed = False
        
    def get_blit_obj(self):
        return (self.button_obj, self.button_rect_obj)
        
    def clicked(self, mouse_x, mouse_y, mouse_clicked):
        if self.button_rect_obj.collidepoint((mouse_x, mouse_y)):
            if self.highlight_effect:
                    if self.changed == False:
                        self.button_obj = self.font_obj.render(self.text, ANTIALLIASING, self.text_color, self.highlight_color)
                        self.changed = True
            return mouse_clicked
        else:
            if self.changed:
                self.button_obj = self.font_obj.render(self.text, ANTIALLIASING, self.text_color, self.bg_color)
                self.changed = False
        return False
    
    def update(self, mouse_x, mouse_y, mouse_clicked):
        if self.clicked(mouse_x, mouse_y, mouse_clicked):
            self.do() 
    
    def do(self):
        print("Overwrite this!")
    
#class UITextBox:

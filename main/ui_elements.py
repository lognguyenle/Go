from constants import ANTIALLIASING

class UITextBox:
    def __init__(self, text, color, bg_color, font_obj, pos):
        self.pos = pos
        self.font_obj = font_obj
        self.text = text
        self.text_color = color
        self.bg_color = bg_color
        self.feature_obj = self.font_obj.render(self.text, ANTIALLIASING, self.text_color, self.bg_color)
        self.rect = self.feature_obj.get_rect()
        self.rect.topleft = (pos[0], pos[1])
        self.changed = False
        
    def get_blit_obj(self):
        return (self.feature_obj, self.rect)
    
    def update(self, mouse_x, mouse_y, mouse_clicked):
        pass

class UIButton(UITextBox):
    def __init__(self, text, color, highlight, highlight_color, bg_color, font_obj, pos):
        super().__init__(text, color, bg_color, font_obj, pos)
        self.highlight_effect = highlight
        self.highlight_color = highlight_color
        
    def clicked(self, mouse_x, mouse_y, mouse_clicked):
        if self.rect.collidepoint((mouse_x, mouse_y)):
            if self.highlight_effect:
                    if self.changed == False:
                        self.feature_obj = self.font_obj.render(self.text, ANTIALLIASING, self.text_color, self.highlight_color)
                        self.changed = True
            return mouse_clicked
        else:
            if self.changed:
                self.feature_obj = self.font_obj.render(self.text, ANTIALLIASING, self.text_color, self.bg_color)
                self.changed = False
        return False
    
    def update(self, mouse_x, mouse_y, mouse_clicked):
        if self.clicked(mouse_x, mouse_y, mouse_clicked):
            self.do()
    
    def do(self):
        print("Overwrite this!")

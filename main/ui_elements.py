from constants import ANTIALLIASING, WHITE

class UIButton:
    def __init__(self, text, color, highlightColor, fontObj, pos):
        self.pos = pos
        self.fontObj = fontObj
        self.text = text
        self.textColor = color
        self.highlightColor = highlightColor
        self.buttonObj = self.fontObj.render(self.text, ANTIALLIASING, self.textColor, WHITE)
        self.buttonRectObj = self.buttonObj.get_rect()
        self.buttonRectObj.topleft = (pos[0], pos[1])
        
    def getBlitObj(self):
        return (self.buttonObj, self.buttonRectObj)
        
    def clicked(self, mousex, mousey, mouseClicked):
        if self.buttonRectObj.collidepoint((mousex, mousey)):
            self.buttonObj = self.fontObj.render(self.text, ANTIALLIASING, self.textColor, self.highlightColor)
            if mouseClicked:
                return True
        else: 
            self.buttonObj = self.fontObj.render(self.text, ANTIALLIASING, self.textColor, WHITE)
        return False
    

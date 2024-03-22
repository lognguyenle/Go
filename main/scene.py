#Referenced from https://nerdparadise.com/programming/pygame/part7

import constants as const

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
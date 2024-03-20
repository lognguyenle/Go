#Referenced from https://nerdparadise.com/programming/pygame/part7

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
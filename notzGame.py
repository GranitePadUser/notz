from notz import *

class NotzSpriteObject:
        def __init__(self, rootCanvas):
                self.root = rootCanvas
                
        def Draw(self, drwobj):
                self.drwobj = drwobj
        def SetBehavior(self, behavior):
                self.beh = behavior
        def UseBehavior(self, speed, behavior_type):
                self.behSpeed = speed
                self.behType = behavior_type
                self.beh.setup(self.behSpeed, self.drwobj)
                self.beh.do(self.behType)
class Behavior:
        def setup(self, speed, NotzSpriteObject):
                self.obj = NotzSpriteObject
                self.spd = speed
        def do(self, behtype):
                if behtype == "FourDir":
                        self.obj.root.obj.bind_all('<KeyPress>', self.move)
        def move(self, event):
                key = event.keysym
                if key == "Right":
                        self.obj.root.obj.move(self.obj.obj, self.spd, 0)
                if key == "Left":
                        self.obj.root.obj.move(self.obj.obj, -self.spd, 0)
                if key == "Up":
                        self.obj.root.obj.move(self.obj.obj, 0, -self.spd)
                if key == "Down":
                        self.obj.root.obj.move(self.obj.obj, 0, self.spd)

from tkinter import *
class NotzObject:
        """Represents all notz objects which don't need tkinter canvas"""
        def __init__(self, rootWin):
                self.root = rootWin
        def Draw(self, types, value):
                self.type = types
                self.value = value
                ##self.x = x
                ##self.y = y
                if types == "text":
                        self.obj = Label(self.root, text=self.value)
                        self.obj.pack()
                if types == "textedit":
                        self.obj = Text(self.root)
                        self.obj.pack()
class NotzCanvas:
        def __init__(self, root, w=100, h=100):
                self.root = root
                self.w = w
                self.h = h
                self.obj = Canvas(self.root, width=self.w, height=self.h)
                self.obj.pack()
class NotzDrawObject:
        """Represents all notz objects which need tkinter canvas"""
        def __init__(self, rootCanvas):
                self.root = rootCanvas
        def Draw(self, types, x, y, w, h):
                self.type = types
                self.x = x
                self.y = y
                self.h = h
                self.w = w
                if types == "line":
                        self.obj =self.root.obj.create_line(x, y, w, h)
                if types == "rectangle":
                        self.obj = self.root.obj.create_rectangle(x, y, x + w, y + h)

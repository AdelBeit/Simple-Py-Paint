#Author: Adel Beitvashahi

from tkinter import *
import random

class Application(Frame):

    penDown = False
    eraserDown = False
    oldX, oldY = None, None
    colors = ['yellow','black']
    penSize = 2
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Paint")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)        
        self.canvas.bind('<Motion>', self.draw) # draw on canvas
        self.canvas.bind('<ButtonPress-1>', self.penDown) # place the pen
        self.canvas.bind('<ButtonRelease-1>', self.penUp) # pick up the pen
        self.canvas.bind('<Double-Button-3>', self.clear) # clear canvas
        self.canvas.bind('<ButtonPress-3>', self.eraserDown) # place the eraser
        self.canvas.bind('<ButtonRelease-3>', self.eraserUp) # pick up the eraser
        self.canvas.bind('<MouseWheel>', self.changeSize) # change brush size
        self.canvas.pack(fill=BOTH, expand=1)

    def draw(self, event):
        x, y = event.x, event.y
        #for some reason using self.penDown alone will always pass as true
        #during initial call, even though it's initialized as False
        if self.penDown == True:
            self.last = self.canvas.create_line(self.oldX, self.oldY, x, y, width=self.penSize,fill=random.choice(self.colors))
        if self.eraserDown == True:
            items = self.canvas.find_overlapping(max(0, x-(self.penSize//2)), max(0, y-(self.penSize//2)), min(500,x+(self.penSize//2)), min(500,y+(self.penSize//2)))
            for x in items:
                self.canvas.delete(x)
        self.canvas.pack(fill=BOTH, expand=1)
        self.oldX = x
        self.oldY = y
    
    def penDown(self, event):
        self.penDown = True

    def penUp(self, event):
        self.penDown = False

    def clear(self, event):
        self.canvas.delete("all")

    def eraserDown(self, event):
        self.eraserDown = True

    def eraserUp(self, event):
        self.eraserDown = False

    def changeSize(self, event):
        num = event.delta // 120
        self.penSize += num
        if self.penSize > 10:
            self.penSize = 10
        if self.penSize < 1:
            self.penSize = 1
        
root = Tk()

root.title("Paint")
root.geometry('500x500')
root.resizable(width = TRUE, height = TRUE)

app = Application(root)

root.mainloop()


from tkinter import *

class Vehicle:
    def __init__(self, x, y, speed=5):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.x+=self.speed

    def stopMove(self):
        self.x=self.x

class Car(Vehicle):
    width=30
    height=20
    def __init__(self,x,y,speed=5):
        super().__init__(x,y,speed)
      #self.x=x
      #self.y=y
      #self.speed=speed
      #self.width=30

    def draw(self,w):
        if self.speed>=0:
            w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,fill="white")
            w.create_line(self.x + self.width * 0.75, self.y , self.x + self.width * 0.75, self.y+self.height)
        else:
            w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,fill="yellow")
            w.create_line(self.x + self.width * 0.25, self.y, self.x + self.width * 0.25, self.y + self.height)


class Lorry(Vehicle):
    width = 60
    height = 20

    def __init__(self, x, y, speed=5):
        super().__init__(x, y, speed)   #java-> super(...)

    def draw(self, w):
        if self.speed >= 0:
            w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,fill="white")
            w.create_line(self.x + self.width * 0.80, self.y, self.x + self.width * 0.80, self.y + self.height)
        else:
            w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,fill="yellow")
            w.create_line(self.x + self.width * 0.2, self.y, self.x + self.width * 0.20, self.y + self.height)

from tkinter import *
from Lane import *
import time

sleep=0.02

class Frog:
    width = 20
    height = 20
    step = 40

    def __init__(self, x, y, wx1, wy1, wx2, wy2, step):
        self.x = x
        self.y = y
        self.window_x1 = wx1
        self.window_y1 = wy1
        self.window_x2 = wx2
        self.window_y2 = y + self.height  # wy2
        self.step = step

    def finishReached(self):
        if self.y <= self.window_y1:
            # self.y=0
            return True
        return False

    def moveLeft(self):
        self.x -= self.step
        if self.x < self.window_x1:
            self.x = self.window_x1
        time.sleep(sleep)

    def moveRight(self):
        self.x += self.step
        if self.x > self.window_x2 - self.width:
            self.x = self.window_x2 - self.width
        time.sleep(sleep)

    def moveUp(self):
        self.y -= self.step
        if self.y < self.window_y1:
            self.y = self.window_y1
        time.sleep(sleep)


    def moveDown(self):
        self.y += self.step
        if self.y > self.window_y2 - self.height:
            self.y = self.window_y2 - self.height
        time.sleep(sleep)

    def draw(self, w):
        w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="green")

    def collision(self, vehicle):
                if self.y != vehicle.y:
                    return False
                if vehicle.x <= self.x <= (vehicle.x + vehicle.width) or \
                        vehicle.x <= (self.x + self.width) <= (vehicle.x + vehicle.width):
                    return True
                else:
                    return False

import numpy as np
from PIL import Image
class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y+self.width] = self.color

class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.x = x
        self.y = y
        self.side = side
        self.data = np.zeros((self.side, self.side, 3), dtype=np.uint8)
        self.data[:] = self.color


    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y+self.side] = self.color
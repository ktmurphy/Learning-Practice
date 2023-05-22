import numpy as np
from PIL import Image
class Canvas:
    def __init__(self, width, height, color, fileName):
        self.width = width
        self.height = height
        self.color = color
        self.fileName = fileName
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color


    def make(self, fileName):
        img = Image.fromarray(self.data, 'RGB')
        img.save(fileName)
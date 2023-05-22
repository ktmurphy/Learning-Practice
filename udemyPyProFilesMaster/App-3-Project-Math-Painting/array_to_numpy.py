import numpy as np
from PIL import Image

# Create 3d numpy array of zeros, then replace zeros (black pixels) with yellow pixels
data = np.zeros((5,4,3), dtype=np.uint8)
data[:] = [255,255,0]
print(data)

data[1:3] = [255, 0, 0]
data[3:5, 2:4] = [0, 0, 255]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
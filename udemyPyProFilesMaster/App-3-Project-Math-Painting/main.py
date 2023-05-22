
from canvas import Canvas
from shapes import Square, Rectangle
import pyinputplus as pyip

# Select and Create Canvas
canvasWidth = pyip.inputInt("Enter canvas width: ")
canvasHeight = pyip.inputInt("Enter canvas height: ")
canvasColor = pyip.inputMenu(['Black', 'White'], lettered=True)
if canvasColor == 'Black':
    canvasColor = (0,0,0)
else:
    canvasColor = (255,255,255)
canvas = Canvas(height=canvasHeight, width=canvasWidth, color=canvasColor, fileName = 'canvas.png')

# Continue allowing the user to draw shapes (rectangle or square)
while True: 
    print('What would you like to draw? Select "quit" to quit.')
    shapeType = pyip.inputMenu(['Rectangle', 'Square', 'Quit'], lettered=True)
    if shapeType == 'Rectangle':
        rectX = pyip.inputInt(f'What is the starting "x" of your rectangle? Enter an integer between 0 and {canvas.width}: ', min = 0, max = canvas.width)
        rectY = pyip.inputInt(f'What is the starting "y" of your rectangle? Enter an integer between 0 and {canvas.height}: ', min = 0, max = canvas.height)
        rectW = pyip.inputInt(f'What is the width of your rectangle? Enter an integer between 0 and {canvas.width-rectX}: ', min = 0, max = canvas.width-rectX)
        rectH = pyip.inputInt(f'What is the height of your rectangle? Enter an integer between 0 and {canvas.height-rectY}: ', min = 0, max = canvas.height-rectY)
        rectColorR = pyip.inputInt(f'What is the color of your rectangle? Enter three numbers (between 0 and 255) one at a time, pretting enter between.  Amount of Red: ', min = 0, max = 255)
        rectColorG = pyip.inputInt(f'Amount of Green: ', min = 0, max = 255)
        rectColorB = pyip.inputInt(f'Amount of Blue: ', min = 0, max = 255)
        rectangle = Rectangle(rectX, rectY, rectW, rectH, color=(rectColorR, rectColorG, rectColorB))
        rectangle.draw(canvas)

    if shapeType == 'Square':
        squareX = pyip.inputInt(f'What is the starting "x" of your square? Enter an integer between 0 and {canvas.width}: ', min = 0, max = canvas.width)
        squareY = pyip.inputInt(f'What is the starting "y" of your square? Enter an integer between 0 and {canvas.height}: ', min = 0, max = canvas.height)
        squareSide = pyip.inputInt(f'What is the side length of your square? Enter an integer between 0 and {max(canvas.width-squareX, canvas.height-squareY)}: ', min = 0, max = max(canvas.width-squareX, canvas.height-squareY))
        squareColorR = pyip.inputInt(f'What is the color of your square? Enter three numbers (between 0 and 255) one at a time, pretting enter between.  Amount of Red: ', min = 0, max = 255)
        squareColorG = pyip.inputInt(f'Amount of Green: ', min = 0, max = 255)
        squareColorB = pyip.inputInt(f'Amount of Blue: ', min = 0, max = 255)
        square = Square(squareX, squareY, squareSide, color=(squareColorR, squareColorG, squareColorB))
        square.draw(canvas)   

    if shapeType == 'Quit':
        break


canvas.make('canvas.png')



    








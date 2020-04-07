import turtle, random

myPen = turtle.Turtle()
myPen.speed(200)
colors  = ["red","green","blue","orange","purple","pink","yellow"]

# This function draws a box by drawing each side of the square and using the fill function
def box(boxSize, x, y, depth):
    myPen.color(random.choice(colors))
    myPen.color('black')
    myPen.penup()
    myPen.goto(x-boxSize/2,y-boxSize/2)
    myPen.pendown()
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 90 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 180 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 270 deg.
    myPen.forward(boxSize)
    myPen.end_fill()
    myPen.setheading(0)
    if depth >0:
        box(boxSize/3, x-boxSize, y, depth-1)
        box(boxSize/3, x-boxSize, y+boxSize, depth-1)
        box(boxSize/3, x, y+boxSize, depth-1)
        box(boxSize/3, x+boxSize, y+boxSize, depth-1)
        box(boxSize/3, x+boxSize, y, depth-1)
        box(boxSize/3, x+boxSize, y-boxSize, depth-1)
        box(boxSize/3, x, y-boxSize, depth-1)
        box(boxSize/3, x-boxSize, y-boxSize, depth-1)
#draw the first box
box(200,0,0, 3)


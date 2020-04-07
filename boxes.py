import turtle
PROGNAME = 'Sierpinski Carpet'

myPen = turtle.Turtle()
myPen.speed(100)

def lbox(bs,x,y, col = '#000000'):
    myPen.color(col)
    myPen.penup()
    myPen.goto(x-bs/2,y-bs/2)
    myPen.pendown()
    myPen.forward(bs)
    myPen.left(90)
    myPen.forward(bs)
    myPen.left(90)
    myPen.forward(bs)
    myPen.left(90)
    myPen.forward(bs)
    myPen.setheading(0)
# This function draws a box by drawing each side of the square and using the fill function
def box(boxSize, x, y, depth, col = '#000000'):
    myPen.color(col)
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
    lbox(10,x,y,'#33cc33')
    if depth >0:
        box(boxSize/2, x-(2*boxSize), y, depth-1)
        box(boxSize/2, x+(2*boxSize), y, depth-1)
        box(boxSize/2, x, y+(2*boxSize), depth-1)
        box(boxSize/2, x, y-(2*boxSize), depth-1)
#draw the first box
box(150,0,0, 4,'#cc33cc')


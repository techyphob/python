import turtle
PROGNAME = 'Test'

myPen = turtle.Turtle()
myPen.speed(10)


def box(bs,x,y, col = '#000000'):
    myPen.color(col)
    myPen.goto(x-bs/2,y-bs/2)
    myPen.forward(bs)
    myPen.left(90)
    myPen.forward(bs)
    myPen.left(90)
    myPen.forward(bs)
    myPen.left(90)
    myPen.forward(bs)
    myPen.setheading(0)
    
myPen.goto(-5,-5)
myPen.forward(10)
myPen.left(90)
myPen.forward(10)
myPen.left(90)
myPen.forward(10)
myPen.left(90)
myPen.forward(10)
myPen.setheading(0)

box(100,0,0)
box(200,0,0,'#cc33cc')

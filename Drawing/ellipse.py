import turtle
from math import cos, sin, radians
t = turtle.Turtle()
t.speed(0)

def ellipse(a, b, h=0, k=0, r=0):
  r1 = radians(r)
  t.penup()
  for i in range (0, 361):
    x, y = a * cos(radians(i)), b * sin(radians(i))
    x1 = x * cos(r1) + y * sin(r1)
    y1 = y * cos(r1) - x * sin(r1)
    t.goto(h + x1, k + y1)
    t.pendown()

for r in range (0, 361, 15):
  ellipse(25, 100, -100, -100, r)

ellipse(25, 100, -100, -100, 90)

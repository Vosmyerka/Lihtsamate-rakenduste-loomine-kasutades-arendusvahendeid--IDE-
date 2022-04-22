import turtle
from random import randint, choice
 
n = 0

turtle.colormode(255)
#turtle.bgcolor("black")

while (n < 100):
  turtle.pensize(randint(10, 50))
  turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
  rand = randint(1, 2)
  turtle.speed(100)
  turtle.forward(randint(1, 100))
  if (rand == 1):
    turtle.left(randint(1, 360))
  else:
    turtle.right(randint(1, 360))
  n = n + 1

turtle.done()
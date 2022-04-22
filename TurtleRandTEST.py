import turtle
from random import randint, choice
 
n = 0

turtle.mode("logo")
turtle.speed(100)
turtle.colormode(255)
#turtle.bgcolor("black")

while (n < 200):
  turtle.pensize(randint(10, 50))
  turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
  rand = randint(1, 2)
  turtle.forward(randint(1, 100))
  if (rand == 1):
    turtle.left(randint(1, 360))
  else:
    turtle.right(randint(1, 360))
  
  while (turtle.xcor() >= 950):
    turtle.penup(),
    turtle.home(),
    turtle.pendown()
  while (turtle.ycor() >= 500):
    turtle.penup(),
    turtle.home(),
    turtle.pendown()
  while (turtle.xcor() <= -950):
    turtle.penup(),
    turtle.home(),
    turtle.pendown()
  while (turtle.ycor() <= -500):
    turtle.penup(),
    turtle.home(),
    turtle.pendown()

  n = n + 1

turtle.done()
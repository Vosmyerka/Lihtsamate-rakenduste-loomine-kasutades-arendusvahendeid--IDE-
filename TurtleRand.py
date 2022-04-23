import turtle
from random import randint, choice
from tkinter import *

#^^^^^^^^^^^^^^^^^^^^^^^^^IMPORT^^^^^^^^^^^^^^^^^^^^^^^^^^

#--------------------------VAR----------------------------

n = 0


#------------------------SETTINGS-------------------------

turtle.mode("logo")                                      # If mode = logo, then turtle looks to North direction, otherwise it looks to East
turtle.speed(0)                                          # Speed of turtle movement, 0 = fastest
turtle.hideturtle()                                      # Hides turtle on the canvas
turtle.colormode(255)                                    # Color mode, 255 = RGB
turtle.bgcolor("white")                                  # Background color

actions = 100                                            # How many moves will make the turtle !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#------------------------MAIN-LOOP------------------------

while (n < actions):

#-----------------------VAR-IN-WHILE----------------------

  allcolors = randint(1, 255), randint(1, 255), randint(1, 255)
  redcolors = randint(1, 255), 0, 0
  greencolors = 0, randint(1, 255), 0
  bluecolors = 0, 0, randint(1, 255)

  rand = randint(1, 2)

#---------------------------------------------------------
  turtle.pensize(randint(10, 50))                        # Write here the randomization of pen size
  turtle.pencolor(allcolors)                             # Write here the color which you want from part VAR-IN-WHILE
  turtle.forward(randint(1, 200))                        # Write here the randomization of move length
  
  if (rand == 1):
    turtle.left(randint(1, 360))
  else:
    turtle.right(randint(1, 360))
  
#--------------------------------#
  while (turtle.xcor() >= 950):  #-------------------------
    turtle.penup(),              #                        |
    turtle.home(),               #                        |
    turtle.pendown()             #                        |
  while (turtle.ycor() >= 500):  #-------------------------
    turtle.penup(),              #                        |
    turtle.home(),               #                        |
    turtle.pendown()             #                        |
  while (turtle.xcor() <= -950): #-------------------------------------- A BORDER, when turtle hits the border it teleports in the begining 
    turtle.penup(),              #                        |
    turtle.home(),               #                        |
    turtle.pendown()             #                        |
  while (turtle.ycor() <= -500): #-------------------------
    turtle.penup(),              #                        |
    turtle.home(),               #                        |
    turtle.pendown()             #-------------------------
#--------------------------------#

  n = n + 1
  print(n)

if (n == actions):
  print("Done")

turtle.done()
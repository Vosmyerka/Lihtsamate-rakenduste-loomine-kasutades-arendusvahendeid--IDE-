import turtle
from random import randint
 
tur = turtle.Turtle()
  
def draw(spce,a):
  for i in range(a):
    for j in range(a):
        
        tur.dot()
          
        tur.forward(spce)
    tur.backward(spce*a)
      
    tur.right(90)
    tur.forward(spce)
    tur.left(90)
 
tur.penup()
draw(10,8) 

tur.hideturtle()
turtle.done()
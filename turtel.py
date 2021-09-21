import turtle
from random import randint

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

def escalier(nbmarche):
  turtle.left(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  
  if nbmarche==1:
    return
  return escalier(nbmarche-1)
  
    
def carre(nombrefois):

  turtle.forward(100-20*nombrefois)
  turtle.left(90)
  turtle.forward(100-20*nombrefois)
  turtle.left(90)
  turtle.forward(100-20*nombrefois +10)
  turtle.left(90)
  turtle.forward(100-20*nombrefois +10)
  turtle.left(90)
  if nombrefois==1:
    return
  return carre(nombrefois-1)
  
def octo(nombrefois):

  turtle.forward(100-20*nombrefois)
  turtle.left(60)
  turtle.forward(100-20*nombrefois)
  turtle.left(60)
  turtle.forward(100-20*nombrefois)
  turtle.left(60)
  turtle.forward(100-20*nombrefois+(5*(1/nombrefois)))
  turtle.left(60)
  turtle.forward(100-20*nombrefois+(10*(1/nombrefois)))
  turtle.left(60)
  turtle.forward(100-20*nombrefois+(10*(1/nombrefois)))
  turtle.left(60)

  if nombrefois==1:
    return
  return octo(nombrefois-1)
  
octo(3)

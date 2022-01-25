from turtle import *


def arbre(n, taille):
    if n == 0:
        color("green")
        forward(taille)
        backward(taille)
        color("brown")
    else:
        forward(taille)
        left(45)
        arbre(n - 1, taille / 2)
        right(90)
        arbre(n - 1, taille / 2)
        left(45)
        backward(taille)
        
        
setpos(0, -100)
setheading(90)
speed(0)

pensize(2)
arbre(7, 200)

end_fill()
done()
exitonclick()

import turtle
from random import *

toto = turtle.Turtle()

def figura(lado, angulo):
    """ Desenha uma figura com uso da recursividade, de lado = lado e angulo = angulo"""
    if lado:
        toto.forward(lado)
        toto.right(angulo)
        figura(lado-1, angulo)

    return 0

# figura(30, 45)
# figura(30, 75)
# figura(100, 75)

def figura_com_lado(lado, angulo, inc):
    """
        Desenha uma figura com lado = lado e angulo = a angulo,
        sendo que o lado aumenta/diminui conforme inc
    """
    if lado:
        toto.forward(lado)
        toto.right(angulo)
        figura_com_lado(lado - inc, angulo, inc)

# figura_com_lado(100, 46, 2)

def figura_lado_ang(lado, angulo, incli, incre):
    """
        Desenha uma figura de lado = lado e angulo = angulo,
        semdp que tanto o lado com o angulo variam
    """
    if lado:
        toto.forward(lado)
        toto.right(angulo)
        figura_lado_ang(lado + incre, angulo + incli, incre, incli)

# figura_lado_ang(100, 50, 1, 2)


def piramide(niveis, lado):
    """
        Desenha uma piramide do tipo:
                    __
                __      __
            __      __      __
        __      __      __      __
    """
    if niveis == 1: linha_rec(1, lado)
    else:
        piramide(niveis - 1, lado)
        toto.penup()
        toto.setx(toto.xcor() - ((niveis - 2) * lado) - lado / 2)
        toto.sety(toto.ycor() - lado)
        toto.pendown()
        linha_rec(niveis, lado)

def linha_rec(n, lado):
    if n == 1: quadrado(lado)
    else:
        linha_rec(n - 1, lado)
        toto.penup()
        toto.setx(toto.xcor() + lado)
        toto.pendown()
        quadrado(lado)

def quadrado(lado):
    c = randint(0, 255)
    turtle.Screen().colormode(255)
    toto.fillcolor(c,c,c)
    toto.begin_fill()
    for i in range(4):
        toto.forward(lado)
        toto.right(90)
    toto.end_fill()

piramide(5, 50)


turtle.Screen().exitonclick()
import turtle
from random import *

t = turtle.Turtle()


def arvore(n, lado):
    """
        Desenha uma arvore com n ramificações

    """
    def s(x=500, y=0):
        t.penup()
        t.setx(x)
        t.sety(y)
        t.pendown()

    for i in range(n, 0, -1):
        if i == n:
            s()
            t.seth(90)
            t.forward(lado)
        else:
            ang = randint(30,80)

            x = t.xcor()
            y = t.ycor()
            s(x,y)
            t.seth(ang)
            t.forward(lado)
            s(x, y)
            t.seth(180 - ang)
            t.forward(lado)
            lado /= 2

# arvore(10, 100)



def tree(length,n):
    """ paints a branch of a tree with 2 smaller branches, like an Y"""
    if n== 1:
           return       # escape the function
    t.forward(length)        # paint the thik branch of the tree
    t.left(45)          # rotate left for smaller "fork" branch
    tree(length * 0.5,n -1)      # create a smaller branch with 1/2 the lenght of the parent branch
    t.right(90)         # rotoate right for smaller "fork" branch
    tree(length * 0.5,n - 1)      # create second smaller branch
    t.left(45)          # rotate back to original heading
    t.backward(length)       # move back to original position
    return              # leave the function, continue with calling program

# tree(50, 10)

t.lt(90)

lv = 13
l = 120
s = 17

t.width(lv)

t.penup()
t.bk(l)
t.pendown()
t.fd(l)

def arvore2(nivel, tamanho, ang, racio):
    if nivel >= 0:
        pass

turtle.Screen().exitonclick()

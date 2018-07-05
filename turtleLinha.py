import turtle

def desenha_linha(turtle, x1, y1, x2, y2):
    """ Desenha uma linha que vai dos pontos (x1, y2) a (x2, y2) """
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)
    turtle.up()
    turtle.forward(100000000)

if __name__ == '__main__':
    turtle.setworldcoordinates(-1000, -1000, 1000, 1000)
    toto = turtle.Turtle()


    desenha_linha(toto, 100,100,-100,-100)
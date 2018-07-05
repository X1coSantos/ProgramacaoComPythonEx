import turtle

toto = turtle.Turtle()

def quadrado(lado):
    """ Desenha um quadrado de lado = lado """
    toto.forward(lado)
    toto.right(90)
    toto.forward(lado)
    toto.right(90)
    toto.forward(lado)
    toto.right(90)
    toto.forward(lado)
    toto.right(90)

def quadrado2(lado):
    """ Desenha um quadrado de lado = lado """
    for i in range(4):
        toto.forward(lado)
        toto.right(90)

def quadrado3(lado, x_cor, y_cor, angulo):
    """ Desenha um quadrado nas coordenadas (x_cor, y_cor) com o angulo inicial = angulo """

    # Preparação
    toto.penup()
    toto.goto(x_cor, y_cor)
    toto.setheading(angulo)
    toto.pendown()
    # Desenha
    for i in range(4):
        toto.forward(lado)
        toto.right(90)


def triangulo(lado):
    """ Desenha um triangulo de lado = lado"""
    for i in range(3):
        toto.forward(lado)
        toto.right(120)


def pentagono(lado):
    """ Desenha um pentagono de lado  = lado """
    for i in range(5):
        toto.forward(lado)
        toto.right(72)


def poligno_regular(lado, n_lados):
    """ Desenha um poligno regular de n_lados lados com lado = lado """
    angulo = 360 / n_lados
    for i in range(n_lados):
        toto.forward(lado)
        toto.right(angulo)


poligno_regular(30, 67)






toto.penup()
toto.forward(1000000000000)

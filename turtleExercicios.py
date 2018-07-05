import turtle
from random import randint
import math

turtle.setworldcoordinates(-1000, -1000, 1000, 1000)

toto = turtle.Turtle()

def estrela(lado):
    """ Desenha uma estrela de lado = lado"""
    for i in range(5):
        toto.forward(lado)
        toto.right(144)


def estrelaV2(n, lado_inicial, x):
    """ Desenha uma estrela com n lados, de lado inicial = lado_inicial, o lado aumenta x por cada viragem """
    for i in range(n):
        toto.forward(lado_inicial)
        toto.right(144)
        lado_inicial += x


def random_walk(n):
    """ Cria um caminho aleatorio de n "ruas " """
    for i in range(n):
        tam = randint(30, 100)
        ang = randint(1, 360)
        toto.forward(tam)
        toto.right(ang)


def random_walkv2(n):
    """ Cria um caminho aleatorio de n ruas, mas apenas anda em angulos de 90 graus """

    angulos = [0, 45, 90, 135, 180, 225, 270, 315]
    for i in range(n):
        tam = randint(10,40)
        ang = angulos[randint(0, len(angulos) - 1)]
        if(toto.xcor() > 1000):
            toto.goto(randint(970,1000), toto.ycor())
        elif(toto.xcor() < -1000):
            toto.goto(randint(-1000,-970), toto.ycor())
        elif(toto.ycor() > 1000):
            toto.goto(toto.xcor(), randint(970,1000))
        elif(toto.ycor() < -1000):
            toto.goto(toto.xcor(), randint(-1000, -970))
        toto.forward(tam)
        toto.right(ang)


def random_walkv3(n_lados, distancia, speed):
    """ Caminho aleatorio com numero de lados = n_lados e distancia constante entre eles de distancia
        Definição de caminho aleatório:
            - Há um ponto de partida.
            - A distância de um ponto no caminho até o próximo é constante.
            - A direção de um ponto no caminho para o próximo é escolhido aleatoriamente,
            e nenhuma direção é mais provável do que outra. """
    viragem = [0, 90, 180, 270]
    zero = 0
    noventa = 0
    centoOitenta = 0
    duzentosSetenta = 0

    toto.speed(speed)

    for i in range(n_lados):
        ranRight = randint(0, len(viragem) - 1)
        toto.forward(distancia)
        toto.right(viragem[ranRight])
        if(ranRight == 0): zero += 1
        elif(ranRight == 1): noventa += 1
        elif(ranRight == 2): centoOitenta += 1
        elif(ranRight == 3): duzentosSetenta += 1

        print(f"0: {zero}\n90: {noventa}\n180: {centoOitenta}\n270: {duzentosSetenta}")


def circulo(n, raio_inicial, aumento, speed):
    """ Desenha n circulos com raio cada vez maior  """
    toto.speed(speed)
    for i in range(n):
        toto.circle(raio_inicial)
        raio_inicial += aumento


def quadrados(n, lado_inicial, aumento, speed):
    """ Desenha n quadrados de lado inicial = lado_inicial, aumentando aumento a cada novo quadrado """
    toto.speed(speed)
    for i in range(n):
        toto.forward(lado_inicial)
        toto.right(90)
        lado_inicial += aumento


def curvas_parametricas(n, speed):
    x_x = 0
    toto.speed(speed)

    lista_cores = ["red", "blue", "yellow"]
    lista = []
    x = 0

    for i in range(n):
        x += 0.001
        y = math.sin(40 * x) * math.sin(72 * x)
        lista.append(f"{x},{y}")
        toto.penup()
        toto.goto(x, y)
        toto.pendown()
        toto.dot(10, (lista_cores[randint(0, len(lista_cores) - 1)]))
        print(str(x) + ", " + str(y))
        x_x += 1
        print(lista)


def cena_esquisita(n, inicio, fim, speed):
    toto.speed(speed)
    turtle.setworldcoordinates(-10, -10, 10, 10)
    x = inicio
    tam = (fim - inicio) / n

    for i in range(n):
        toto.goto(x, x - 1.6 * math.cos(24 * x))
        x += tam


cena_esquisita(100, -10, 10, 10)
#https://blogs.scientificamerican.com/guest-blog/making-mathematical-art/


toto.forward(10000000)
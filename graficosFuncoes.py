import turtle
import math

def grafico(turtle, funcao, inicio, fim, n):
    """ Desenhao gráfico da função f, entre inicio e fim usando n segmentos """

    # Tamanho dos segmentos
    tam_seg = (fim - inicio) / n

    # Posiciona-se
    x = inicio
    turtle.up()
    turtle.goto(x, funcao(x))
    turtle.down()

    # Desenha
    for conta in range(n):
        x += tam_seg
        turtle.goto(x, funcao(x))

if __name__ == '__main__':
    turtle.setworldcoordinates(-math.pi, -2, math.pi, 2)

    toto = turtle.Turtle()
    toto.pen(pensize=5, pencolor="gray")
    grafico(toto, math.cos, -math.pi, math.pi, 50)
    toto.hideturtle()


    toto.up()
    toto.forward(101101023442)
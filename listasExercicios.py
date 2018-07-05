import math, turtle
from random import *

def AreaTrianguloHeron(a, b, c):
    """ Calcula a area de um triangulo com a formula de heron """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

AreaTrianguloHeron(150,150,150)


def comprimento_escada(altura, inclinacao):
    """ Calcula o comprimento da escada dada a altura e inclinação """
    inclinacao = math.pi / 180 * inclinacao
    return altura / math.sin(inclinacao)

comprimento_escada(10, 90)


def batimento_cardiaco_medio_maximo(idade):
    """ Calcula o valor medio do batimento cardiaco máximo """
    return 163 + 1.16 * idade - 0.018 * pow(idade, 2)

batimento_cardiaco_medio_maximo(18)


def rendimento_ano(v, t, a):
    """
        v -> valor inicial
        t -> taxa de juro
        a -> anos passados
        formula -> v * (1 + t)^a
    """
    return v * (pow(1 + t, a))

rendimento_ano(1000, 0.2, 10)


def rendimento_mensal(v, t, a, n):
    """
        v -> valor inicial
        t -> taxa de juro
        a -> anos passados
        n -> meses
        formula -> v * (1 + 1 / n)^n*a
    """
    return v * pow(1 + 1 / n, n * a)

rendimento_mensal(1000, 0.02, 2, 2)
rendimento_mensal(1000, 0.02, 2, 12)

def log_formula():
    """ Formula com log que nao sei o que faz """
    x = 0
    r = 0
    for i in range(6):
        x += 1
        r += x * math.log(x, 2)
    return r

log_formula()

def incripta(texto_normal):
    """ Incripta texto """
    comp = len(texto_normal)

    # Seleciona todas as letras a partir do 0, até á comp (que vai ser a ultima) de 2 em 2, ou seja, as pares
    car_pares = texto_normal[0:comp:2]
    # Seleciona todas as letras a partir do 1, até á comp (que vai ser a ultima) de 2 em 2, ou seja, as impares
    car_impares = texto_normal[1:comp:2]

    texto_incriptado =  car_pares + car_impares
    return texto_incriptado

incripta("Testar isto aqui")


def incripta2(texto_normal):
    """ Incripta o texto mas com contador """
    car_pares = ""
    car_impares = ""
    contador = 0

    for car in texto_normal:
        # se for par
        if(contador % 2 == 0):
            car_pares += car
        else:
            car_impares += car
        contador += 1

    texto_incriptado = car_impares + car_pares
    return texto_incriptado

incripta2("ABABABABABABA")


def desincripta_pares_impares(texto_incriptado):
    """ Desincripta texto incriptado da forma dos pares e impares """

    tam = len(texto_incriptado)
    final = ""

    if tam % 2 == 0:
        metade = tam // 2
    else:
        metade = tam // 2 + 1

    pares = texto_incriptado[0:metade:1]
    impares = texto_incriptado[metade:tam:1]

    for i in range(0, len(impares)):
        final += pares[i] + impares[i]

    if tam % 2 != 0: final += pares[-1]
    return final

desincripta_pares_impares(incripta("FANCISCo"))


def incripta_ci(texto_normal, chave):
    """ Incripta um texto pelo metodo de chave de substituição(ci) """
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz0123456789 "
    texto_incriptado = ""

    for car in texto_normal:
        indice = alfabeto.find(car)
        texto_incriptado += chave[indice]

    return texto_incriptado

incripta_ci("abcde", "XYZabcGp4qrs3HIJ2KLM1Nd0efghi5jOklm7STUWx8yznot6uwABC9DEFPQR ")


def desincripta_ci(texto_incriptado, chave):
    """ Desincripta texto incriptado pelo metodo da chave de substituição """
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz0123456789 "
    texto_desincriptado = ""

    for car in texto_incriptado:
        indice = chave.find(car)
        texto_desincriptado += alfabeto[indice]

    return texto_desincriptado

desincripta_ci(incripta_ci("abcde", "XYZabcGp4qrs3HIJ2KLM1Nd0efghi5jOklm7STUWx8yznot6uwABC9DEFPQR "),
                     "XYZabcGp4qrs3HIJ2KLM1Nd0efghi5jOklm7STUWx8yznot6uwABC9DEFPQR ")


def substituir_vogais_por_espacos(texto):
    """ Substitui as vogais de um texto por espaços em branco """
    vogais = ("a", "e", "i", "o", "u")
    t = texto.lower()

    for car in t:
        if car in vogais:
            t = t.replace(car, " ", len(texto))

    return t

substituir_vogais_por_espacos("TESTE")


def imprime_subcadeias(texto, n):
    """ Imprime todas as subcadeias de texto de comprimento igual ao numero """
    r = ""
    x = 0
    for car in range(0, len(texto) - n + 1):
        r += texto[x:n:1]
        n += 1
        x += 1
        r += "\n"

    return r

imprime_subcadeias("Monty Python", 3)


def imprime_subcadeiasV2(texto, n):
    """ Imprime todas as subcadeias de texto de comprimento igual ao numero """
    for car in range(len(texto) - n + 1):
        print(texto[car:car+n])

#imprime_subcadeiasV2("Monty Python", 3)


def prefixos_cadeia(texto):
    """ Imprimte todos os prefixos de uma cadeia """
    for c in range(len(texto)):
        print(texto[:c+1])

#prefixos_cadeia("Monty Python")


def sufixos_cadeia(texto):
    """ Imprime todos os sufixos de uma cadeia """
    for c in range(len(texto)):
        print(texto[-c-1:])

#sufixos_cadeia("Monty Python")


def sufixos_cadeiaV2(texto):
    """ Imprime todos os sufixos de uma cadeia """
    for c in range(len(texto), 0, -1):
        print(texto[c-1:])

#sufixos_cadeiaV2("Monty Python")


def simulador_tartaruga(distancia):
    """
        Simula o comportamento de uma tartaruga
        Ações -> f, t, e d
            f - Move-se para a frente
            t - Move-se para tras
            e - roda á esquerda
            d - roda á direita
    """
    t = turtle.Turtle()
    codigo_genetico = ""

    for i in range(1000):
        a = random.randint(1,4)
        if a == 1: codigo_genetico += "f"
        if a == 2: codigo_genetico += "t"
        if a == 3: codigo_genetico += "e"
        if a == 4: codigo_genetico += "d"

    ang = random.randint(1,90)

    for gene in codigo_genetico:
        if gene == "f" : t.forward(distancia)
        if gene == "t" : t.backward(distancia)
        if gene == "e" : t.left(ang)
        if gene == "d" : t.right(ang)

    turtle.Screen().exitonclick()

#simulador_tartaruga(10)


def leibniz_pi(num_termos):
    """ Calculo de pi de acordo com leibniz """
    acum = 0.0
    sinal = 1
    for i in range(1, 2 * num_termos + 1 ,2):
        acum += sinal * (1.0/i)
        sinal *= -1
    return 4 * acum

leibniz_pi(5)


def leibniz_piV2(num_termos):
    """ Calculo de pi de acordo com leibniz 2 """
    acum = 0
    for i in range(num_termos):
        acum += ((-1)**i) * (1 / (2 * i + 1))

    return 4 * acum

leibniz_piV2(100)

def assert_v1(n):
    """ Teste com assert """
    assert n < 100
    print("ola")

#assert_v1(100)


def vencimento_liquido(vencimento_bruto):
    """
        Calcula o vencimento liquido , dado o Vencimento Bruto
        Vencimento Bruto =
            - 25% IRS
            - 5% Segurança social
            - 10% Caixa Nacional de Aposentações
    """

    def p(percentagem):
        """ Calcula o valor da percentagem de vencimento_bruto """
        return percentagem * vencimento_bruto / 100

    vencimento_liquido = vencimento_bruto - p(25) - p(5) - p(10)

    return vencimento_liquido

vencimento_liquido(100)


def palavras_amigas(p1, p2):
    """
        Duas palavras sao amigas se:
        - Tiverem o mesmo comprimento
        - Os caracteres DA MESMA POSIÇÃO, diferirem em menos de 10%
        retorna true ou false
    """

    car_iguais = 0
    car_diferentes = 0

    if len(p1) == len(p2):
        for i in range(len(p1)):
            if p1[i] == p2[i]: car_iguais += 1
            else: car_diferentes += 1

        p_iguais = 100 - ( car_iguais * 100 / len(p1))

        if p_iguais < 10:
            print(f"São AMIGAS, apenas diferem em {p_iguais}")
            return True
        else:
            print(f"Não sao AMIGAS, diferem em {p_iguais}")
            return False

    else:
        print(f"Não sao AMIGAS, diferem em comprimento {len(p1)} - {len(p2)}")
        return False

# palavras_amigas("aaaaaaaaaaa", "aaaaaaaaaba")


def prob_sair_par_dado_6_lados(n):
    """ Probabilidade de sair par lançando um dado de 6 lados n vezes"""

    n_pares = 0

    for i in range(n):
        l_dado = randint(1,6)
        if l_dado % 2 == 0:
            n_pares += 1

    perc = n_pares * 100 / n

    return perc

prob_sair_par_dado_6_lados(1000)


def fatorial(n):
    """
        Calcula o fatorial de um numero n
        fac(n) = n * (n-1) * (n - 2)
    """
    fat = 1
    for i in range(n):
        fat *= (n - i)

    return fat

fatorial(3)


def numeros_perfeitos(a, b):
    """ Determina os numeros perfeitos no intervalo [a, b] """



    for i in range(a, b + 1):
        if i % 10000 == 0: print(i)

        soma_divisores = 0
        for j in range(i-1, 0, -1):
            if i % j == 0:
                soma_divisores += j
                if soma_divisores > i:
                    break


        if soma_divisores == i:
            print(f"{i} é perfeito")

# numeros_perfeitos(1, 77232918)


def padraoA(n):
    """
        Cria um padrão do tipo:
        1
        1 2
        1 2 3
        1 2 3 4 ...
    """
    for i in range(1, n + 1):
        for j in range(i):
            print(j + 1, end=" ")
        print("", end="\n")

# padraoA(6)


def padraoB(n):
    """
        Cria um padrao do tipo:
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    """
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("", end="\n")

#padraoB(6)


def padraoC(n):
    """
        Cria um padrão do tipo:
                1
              2 1
            3 2 1
          4 3 2 1
        5 4 3 2 1
    """
    for i in range(1, n + 1):
        for k in range(n - i):
            print(" ", end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print("", end="\n")

# padraoC(5)


def desenhar_grelha(l, a, tam):
    """
        Desenha uma grelha de dimensoes l * a, sendo o tamanho de cada célula, tam
        Passeio aleatório, pode-se mover dentro da grelha, das seguintes maneiras:
            - Norte, oeste, sul, este
    """
    turtle.setworldcoordinates(0, -1000, 1000, 0)
    t = turtle.Turtle()
    t.speed(100)

    def desenha_linhas():
        """ Desenha as linhas da grelha """
        for linha in range(l + 1):
            t.forward(a * tam)
            t.right(90)
            t.penup()
            t.forward(tam)
            t.left(90)
            t.backward(a * tam)
            t.pendown()

    def desenha_colunas():
        """ Desenha as colunas da grelha """
        t.penup()
        t.goto(0,0)
        t.pendown()

        for coluna in range(a + 1):
            t.right(90)
            t.forward(l * tam)
            t.penup()
            t.left(90)
            t.forward(tam)
            t.right(90)
            t.backward(l * tam)
            t.pendown()
            t.left(90)

    desenha_linhas()

    desenha_colunas()

    def caminho_aleatorio():
        """ Caminho aleatorio em cima da grelha """
        t.speed(100)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.dot(10, "red")
        t.pensize(2)
        x = 0
        y = 0
        tam_grelha_largura = tam * l
        tam_grelha_altura = tam * a

        while True:
            if x == 0 and y == 0:
                n = randint(1,2)
                if n == 1:
                    t.setheading(0)
                    x += tam
                if n == 2:
                    t.setheading(270)
                    y -= tam
                #print("1")

            elif x == 0 and y == -tam_grelha_altura:
                n = randint(1,2)
                if n == 1:
                    t.setheading(0)
                    x += tam
                if n == 2:
                    t.setheading(90)
                    y += tam

            elif x == tam_grelha_largura and y == 0:
                n = randint(1,2)
                if n == 1:
                    t.setheading(180)
                    x -= tam
                if n == 2:
                    t.setheading(270)
                    y -= tam
                #print("3")

            elif x == tam_grelha_largura and y == -tam_grelha_altura:
                n = randint(1,2)
                if n == 1:
                    t.setheading(90)
                    y += tam
                if n == 2:
                    t.setheading(180)
                    x -= tam
                #print("4")

            elif x > 0 and y < tam_grelha_altura and y == 0:
                n = randint(1,3)
                if n == 1:
                    t.setheading(0)
                    x += tam
                if n == 2:
                    t.setheading(180)
                    x -= tam
                if n == 3:
                    t.setheading(270)
                    y -= tam
                #print("5")

            elif x > 0 and x < tam_grelha_largura and y == -tam_grelha_altura:
                n = randint(1, 3)
                if n == 1:
                    t.setheading(0)
                    x += tam
                if n == 2:
                    t.setheading(90)
                    y += tam
                if n == 3:
                    t.setheading(180)
                    x -= tam
                #print("6")

            elif y < 0 and y > -tam_grelha_altura and x == 0:
                n = randint(1, 3)
                if n == 1:
                    t.setheading(0)
                    x += tam
                if n == 2:
                    t.setheading(90)
                    y += tam
                if n == 3:
                    t.setheading(270)
                    y -= tam
                #print("7")

            elif y < 0 and y > -tam_grelha_altura and x == tam_grelha_largura:
                n = randint(1, 3)
                if n == 1:
                    t.setheading(90)
                    y += tam
                if n == 2:
                    t.setheading(180)
                    x -= tam
                if n == 3:
                    t.setheading(270)
                    y -= tam
                #print("8")

            else:
                n = randint(1,4)
                if n == 1:
                    t.setheading(0)
                    x += tam
                elif n == 2:
                    t.setheading(90)
                    y += tam
                elif n == 3:
                    t.setheading(180)
                    x -= tam
                elif n == 4:
                    t.setheading(270)
                    y -= tam
                #print("9")


            t.forward(tam)
            print(f"{x},{y}")

    caminho_aleatorio()


    turtle.Screen().exitonclick()

#desenhar_grelha(40, 40, 25)


from random import *
import matplotlib.pyplot

cadeia = "Homem Aranha"

cadeia[3]

cadeia[1:4]

max(cadeia)
min(cadeia)

cadeia.index("e")
cadeia.count("m")


frase = "Ola liliana, isto é uma frase! "
fraseSplit = frase.split()

fraseJoin = " ".join(fraseSplit)

def lista_randoms_ints(n):
    """ Cria uma lista de inteiros random, de tamanho n """
    lista = []
    for i in range(n):
        lista.append(randint(1,100))

    return lista

def imprime_lista(lista):
    """ Imprime uma lista """
    for i in range(len(lista)): print(lista[i], end=" ")

# imprime_lista(lista_randoms_ints(100))


def lista_randoms_ints_compreensao(n):
    """ Cria uma lista de inteiros random, de tamanho n, por compreensão """
    return [randint(1,100) for i in range(n)]


def quadrados(lista):
    """ Cria uma lista com os quadrados das listas dadas """
    return [lista[i] ** 2 for i in range(len(lista))]

quadrados(lista_randoms_ints(10))


# print([i for elem in [[1,-2,3],[-4,5,-6]] for i in elem if i > 0])


def imprimir_lista_enumerate(lista):
    """ Percorre a lista com enumerate """
    for i, v in enumerate(lista):
        print(i, v)

# imprimir_lista_enumerate(lista=[1,2,3,4,5])


def media(lista):
    """ Calcula a media de uma lista de inteiros """
    soma = 0
    for i in lista:
        soma += i
    return soma / len(lista)

# print(media(lista=[10,5]))


def mediaV2(lista):
    """ Calcula a media de uma lista de inteiros v2 """
    return sum(lista) / len(lista)

# print(mediaV2(lista=[5,10]))


def mediana(lista):
    """
        Calcula a mediana de uma lista de inteiros
        par: 1 2 4 6 7 8
                [   ]
        impar: 1 2 3 4 5
                  [ ]
    """
    meio = len(lista) // 2
    if len(lista) % 2 == 0:
        med = (lista[meio] + lista[meio + 1]) / 2
    else:
        med = lista[meio]

    return med

mediana(lista=[1,2,3,4,5,4,3,2,1])


def grafico_lista(lista):
    """ Mostra um gráfico com os valores da lista """
    plt = matplotlib.pyplot

    plt.xlabel("Dias")
    plt.ylabel("Quantidade")
    plt.title("Baleias")
    plt.plot(lista)
    plt.show()

grafico_lista(lista=[1,2,4,10,2,5,1,5])


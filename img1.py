import random

imagem = [(131,  27, 233), (  4, 243,  68), (195, 107, 123)],\
         [(246, 205, 141), (154,  60, 154), ( 40,  31, 223)]

def mostra_por_linhas(matriz):
    """ Inedxação pelço conteudo """
    for linha in matriz:
        for coluna in linha:
            print(f"{coluna}", end=" ")
        print()


def mostra_por_linhas_b(matriz):
    """ Indexação pela posição """
    for pos_linha in range(len(matriz)):
        for pos_coluna in range(len(matriz[0])):
            print(f"{matriz[pos_linha][pos_coluna]}", end=" ")
        print()

# mostra_por_linhas_b(imagem)


def mostra_por_colunas(matriz):
    """ Indexação pela posição """
    for pos_coluna in range(len(matriz[0])):
        for pos_linha in range(len(matriz)):
            print(f"{matriz[pos_linha][pos_coluna]}", end=" ")
        print()

# mostra_por_colunas(imagem)

#   [ [(131,  27, 233), (  4, 243,  68), (195, 107, 123)],
#   [(246, 205, 141), (154,  60, 154), ( 40,  31, 223)] ]
#   pos_c len(matriz[0]) = 0 1 2
#   pos_l len(matriz) = 0 1
#   m[pos_l][pos_c]
#   m[0][0] = 131
#   m[1][0] = 246
#   m[0][1] = 4
#   m[1][1] = 154
#   m[0][2] = 195
#   m[1][2] = 40


def cria_matriz(n, m, val):
    """ Cria uma matriz nXm sendo que todos os elementos sao iguais a val """
    mat = []
    for j in range(n):
        linha = []
        for i in range(m):
            linha.append(val)
        mat.append(linha)
    return mat

# mostra_por_linhas(cria_matriz(12,7,3))


def cria_matriz_random(n, m, limA, limB):
    """
        Cria uma matriz de tamanho nXm sendo que todos os elementos estao entre limA e limB
        n - numero de linhas
        m - numero de colunas
    """
    mat = []
    for j in range(n):
        linha = []
        for i in range(m):
            val = random.randint(limA, limB)
            linha.append(val)
        mat.append(linha)
    return mat

# mostra_por_linhas(cria_matriz_random(40, 30, 10, 99))


def cria_matriz_b(n, m, val):
    """ Cria uma matriz nXm sendo que todos os elementos sao iguais a val """
    mat = [[val for i in range(m)] for j in range(n)]
    return mat

# mostra_por_linhas(cria_matriz_b(10,10, 3))


def cria_matriz_c(n, m, val):
    """ Cria matriz nXm sendo que todos os elementos sao iguais a val """
    return [[val] * m] * n

# mostra_por_linhas(cria_matriz_c(5, 5, 3))


def soma_matriz(matriz1, matriz2):
    """ Soma duas matrizes da mesma dimensao """
    n_linhas = len(matriz1)
    n_colunas = len(matriz1[0])
    mat = cria_matriz(n_linhas, n_colunas, 0)
    for linha in range(n_linhas):
        for coluna in range(n_colunas):
            mat[linha][coluna] = matriz1[linha][coluna] + matriz2[linha][coluna]
    return mat

#matriz1 = cria_matriz_random(2,2,10,20)
#matriz2 = cria_matriz_random(2,2,10,20)
#mostra_por_linhas(matriz1)
#print()
#mostra_por_linhas(matriz2)
#print()
#mostra_por_linhas(soma_matriz(matriz1, matriz2))


def multiplicacao_matriz(matriz1, matriz2):
    """
        Multiplica a matriz 1 pela matriz 2
        Cij = Aik * Bkj
    """
    n_linhas1   = len(matriz1)
    n_colunas1  = len(matriz1[0])
    n_linhas2   = len(matriz2)
    n_colunas2  = len(matriz2[0])

    mat = cria_matriz(n_linhas1, n_colunas2, 0)
    for j in range(n_linhas1):
        for i in range(n_colunas1):
            val = 0
            for k in range(n_colunas2):
                val += matriz1[i][k] * matriz2[k][j]
            mat[i][j] = val
    return mat

matriz1 = cria_matriz_random(2,2,1,9)
matriz2 = cria_matriz_random(2,2,1,9)
mostra_por_linhas(matriz1)
print()
mostra_por_linhas(matriz2)
print()
mostra_por_linhas(multiplicacao_matriz(matriz1, matriz2))
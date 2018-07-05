def divide(x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        print("Divisao por 0")
        return -1
    else:
        return res

# print(divide(10,1))


def fact_rec(x):
    assert x >= 0, "X TEM DE SER MAIOR QUE 0"
    if x == 0: return 1
    else: return x * fact_rec(x - 1)

#print(fact_rec(7))


def nova_media(lista):
    """
        Doc
    """
    return [sum(lista[:i+1])//len(lista[:i+1]) for i in range(len(lista))]

#print(nova_media([1,2,3]))



def procura_pos(sol_parcial, rainha):
    dim = len(sol_parcial)
    pos = sol_parcial[rainha + 1]
    for j in range(pos, dim):
        if possivel(j, sol_parcial, rainha):
            return j
    return -1

def possivel(pos, sol_parcial, rainha):
    for j in range(rainha):
        if (sol_parcial[j] == pos) or (abs(pos - sol_parcial[j]) == abs(rainha - j)):
            return False
    return True

def n_rainhas(n):
    # Inicialização
    # Rainha i + solução parcial
    x = [-1] * n
    i = 0
    while i >= 0:
        # procura posição, x_i para a rainha de ordem i
        encontra = procura_pos(x, i)
        if encontra:
            # atualizamos vetor solução
            x[i] = encontra
            # nova solução
            if i == (n-i):
                print(x)
                #mostra/guarda nova solução final
            else: # Passa para a rainha seguinte
                i += 1
        else:
            #bactrack
            x[i] = -1
            i -= 1




if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Soma dos inteiros naturais ate n

def somatorio1(n):
    soma = 0
    for i in range(n+1):
        soma += i
    return soma

somatorio1(5)


def somatorio2(n):
    return sum(range(n+1))

somatorio2(5)


def somatorioQuadrados1(n):
    soma = 0
    for i in range(n + 1):
        soma += i ** 2
    return soma

somatorioQuadrados1(3)


def somatorioQuadrados2(n):
    return sum([i ** 2 for i in range(n+1)])

somatorioQuadrados2(3)
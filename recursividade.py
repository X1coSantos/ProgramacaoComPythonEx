def torres_hanobi(n, a, b , c):
    if n == 1:
        print(f"Move disco {n} de {a} para {c}")
    else:
        torres_hanobi(n-1, a, b, c)
        print(f"Move disto {n} de {a} para {c}")
        torres_hanobi(n-1,b,a,c)

# torres_hanobi(3,3,13,1)


def fatorial(n):
    """ Calcula o fatorial de n """
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

fatorial(5)


def soma(m, n):
    if n == 0:
        return m
    else: return 1 + soma(m, n-1)

soma(6,0)

def prod(m, n):
    if n == 0: return 0
    else: return soma(m, prod(m, n-1))

prod(1, 10)


def maximo_divisor_comum(n1, n2):
    """
        Calcula o maximo divisor comum entre dois numeros
        1 - Calcular ps divisores dos dois numeros
        2 - Determinar os comuns
        3 - excolher o max
    """
    d_1, d_2 = [], []
    for i in range(n1, 0, -1):
        if n1 % i == 0: d_1.append(i)

    for j in range(n2, 0, -1):
        if n2 % j == 0: d_2.append(j)

    return max(set(d_1).intersection(d_2))

maximo_divisor_comum(123,453)


def maximo_divisor_comum2(n1, n2):
    """
        Calcula o maximo divisor comum entre dois numeros
        1 - Calcular ps divisores dos dois numeros
        2 - Determinar os comuns
        3 - excolher o max
    """
    d_1, d_2 = [], []
    [d_1.append(i) for i in range(n1, 0, -1) if n1 % i == 0]
    [d_2.append(i) for i in range(n2, 0, -1) if n2 % i == 0]

    return max(set(d_1).intersection(d_2))

maximo_divisor_comum2(23856, 23786)


def mdc(m, n):
    if n == 0:
        return m
    else:
        return mdc(n ,m % n)

mdc(23856,23786)


def fib(n):
    if n == 1 or n == 2: return 1
    else: return fib(n-1) + fib(n-2)

fib(5)


def binomio(n, k):
    if k == 0 or k == n: return 1
    else: return binomio(n-1, k) + binomio(n-1, k-1)

binomio(6,2)


def par(n):
    """ Determina se um numero é par """
    if n < 0: return False
    elif n == 0: return True
    elif impar(n-1): return True
    else: return False

def impar(n):
    """ Determina se um numero é impar """
    if n < 1: return False
    elif n == 1: return True
    elif par(n-1): return True
    else: return False

par(222)


def alterna_plus(lst):
    if len(lst) == 1: return True
    elif lst[0] > lst[1]: return alterna_plus(lst[1:])
    else: return False

def alterna_minus(lst):
    if len(lst) == 1: return True
    elif lst[0] < lst[1]: return alterna_minus(lst[1:])
    else: return False

def alterna(lst):
    if len(lst) == 1: return True
    elif lst[0] > lst[1]: return alterna_minus(lst[1:])
    else: return alterna_plus(lst[1:])

alterna([1,8,2,7])


def procura_s(elem, seq):
    if len(seq) == 0: return False
    elif seq[0] == elem: return True
    else: return procura_s(elem, seq[1:])

procura_s(10,[1,2,3,10,4,5])


def capicua(seq):
    if len(seq) == 0 or len(seq) == 1: return True
    elif seq[0] == seq[-1]: return capicua(seq[1:-1])
    else: return False

capicua("aallaa")


def inverter(string):
    """
        Inverter string
    """

    if len(string) == 0: return string
    else: return inverter(string[1:]) + string[0]

inverter("ola")


def sobe_e_desce(n):
    """ retorna uma lista de numeros de n até 0 e de 0 até n """
    if n == 1: return [1,1]
    else: return [n] + sobe_e_desce(n-1) + [n]

sobe_e_desce(5)


def inter(l1, l2):
    """
        Junta duas listas intercalando os elementos de cada uma, caso uma das listas tenha elementos a mais,
        juntam-se no final
    """
    if l1 == []: return l2
    elif l2 == []: return l1
    else: return [l1[0], l2[0]] + inter(l1[1:], l2[1:])

inter([1,2], [3,4])
inter([1,2,3,4,5,6], [7,8,9])
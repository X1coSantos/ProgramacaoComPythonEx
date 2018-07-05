import time

def anagrama(cad):
    if cad == "": return [cad]
    else:
        resp = []
        for perm in anagrama(cad[1:]):
            for pos in range(len(perm) + 1):
                resp.append(perm[:pos] + cad[0] + perm[pos:])
        return resp

anagrama("cad")


def permutacoes(lst):
    if len(lst) == 0: return [[]]
    else:
        resp = []
        for perm in permutacoes(lst[1:]):
            for pos in range(len(perm) + 1):
                resp.append(perm[:pos] + [lst[0]] + perm[pos:])
        return resp

permutacoes([0,1,2,3,4])

def permuta(lista):
    if len(lista) == 0: return [[]]
    else:
        resp = []
        for perm in permuta(lista[1:]):
            for pos in range(len(perm) + 1):
                resp.append(perm[:pos] + [lista[0]] + perm[pos:])
        return resp

permuta([1,2,3])


def fib(n, dic):
    """ Descobrir o numero de fib para n, recorrendo á memoria """
    if n == 1 or n == 2: return 1
    else:
        if n in dic:
            return dic[n]
        else:
            sol = fib(n-1, dic) + fib(n-2, dic)
            dic[n] = sol
            return sol

print(fib(1, {300: 222232244629420445529739893461909967206666939096499764990979600}))


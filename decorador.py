def decorador(func):
    def interna(x, y):
        print(x, y)
    return interna

def decorador2(func):
    def interna(x):
        return func(x)
    return interna
# decorador = interna -> função decorada
#

@decorador
def soma(x, y):
    return x + y

@decorador2
def quadrado(x):
    return x ** 2




def dec(funcao):
    def interna(x, y, z):
        return funcao(x, y, z)
    return interna

@dec
def XYZ(x, y, z):
    return [x] + [y] + [z]



contador = 0
def decoradorContador(funcao):
    def interna(x, y):
        global contador
        contador += 1
        return funcao(x, y)
    return interna

@decoradorContador
def somas(x, y):
    return x + y


def decorador_contas(func):
    def interna(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return func(x, y)
        else: raise ValueError("DOIS INTEIROS")
    return interna

@decorador_contas
def somas(x, y):
    return x + y

@decorador_contas
def dividir(x, y):
    return x / y

print(somas(2,6))
print(dividir(2,2))

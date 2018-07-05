def decorador(funcao):
    def wrapper(x, y):
        print("OLA")
        return funcao(x, y)
    return wrapper


@decorador
def soma(x, y):
    return x + y

print(soma(2,3))
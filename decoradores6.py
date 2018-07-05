def decorador(funcao):
    def interior(x, y):
        print(funcao.__name__)
        print("teste")
        return funcao(x, y)
    return interior

@decorador
def soma(x, y):
    return x + y

@decorador
def divide(x, y):
    return x / y

print(soma(2,2))
print(divide(2,2))
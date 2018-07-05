def my_max(*valores):
    """
        Qual é o maximo de um numero de valores?
    """
    if not valores: return None
    else:
        maior = valores[0]
        for val in valores[1:]:
            if  val > maior: maior = val
        return maior

print(my_max(1,2,23,3,4,5,6,7,2))


def func(**args):
    """
        Mostra argumentos em forma de dicionarios
    """
    print(args)

func(arg1="teste", arg2="argumento 2", arg3="argumento 3")



def teste(a, *b, c):
    print(a, b, c)

teste(1, (10,21), 12, c= 2)

teste(a = 1, c = 2)


def canal(r, g, b):
    print(r)
    print(g)
    print(b)

canal(255, 255, 255)

pixel = (3,123,6)
canal(*pixel)


def exemplo(a, b, c, d):
    print(a, b, c, d)

dic = {'a': 2, 'b': 3, 'c': 4, 'd': 5}
exemplo(**dic)


def func2(*args, nome):
    print(args)
    print(nome)

func2(1,2,3,4, nome="teste")
# lambda  <parametros> : <expressao>
a = lambda  x, y: x + y
print(a(10,5))

for i in range(4):
    print((lambda x: x ** 2)(i), end=" ")

print("\n")

lista = [(lambda x: x ** 2)(i) for i in range(4)]
print(lista, end="\n")

lista_2 = [lambda x : x ** 2, lambda x : x ** 3, lambda x : x ** 4]
print([lista_2[i](2) for i in [0,1,2]])
print(lista_2[2](3))

print("\n")

def elevado2(n):
    return (lambda x : x ** 2)(n)

print(elevado2(3))

print("\n")

a = (lambda x, y: x if x < y else y)
print(a(10,20))

a = (lambda x : (lambda y : x + y))
print(a(10)(20))

a = (lambda x: (lambda y : (lambda z : x + y + z)))
print(a(5)(10)(20))
def soma(x, y):
    soma.count += 1
    return x + y

soma.count = 0
soma(2,3)

print(soma.count)

string = "Ola a todos isto é a primeira cena de cada"
lista = [palavra[0] for palavra in string.split()]
print(lista)


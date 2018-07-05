# 1
# 2 2
# 3 3 3
# n n n n

def cenas(n):
    for i in range(n+1):
        print(f"{i}" * i)


while True:
    numero = int(input("Numero de vezes"))

    if(numero == 0):
        break
    cenas(numero)
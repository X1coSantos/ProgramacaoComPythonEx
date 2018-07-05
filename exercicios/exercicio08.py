# Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n

def piramide(n):
    for i in range (1, n+1):
        print(f"{i} "*i)

piramide(5)

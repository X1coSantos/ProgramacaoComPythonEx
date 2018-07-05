# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
#  [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deverá terminar quando for lido um número negativo.

num = 1
int1 = 0
int2 = 0
int3 = 0
int4 = 0

while num > 0 and num < 101:
    num = int(input("Insira um numero: "))

    if num > 0 and num < 26:
        int1 += 1
    elif num > 25 and num < 51:
        int2 += 1
    elif num > 50 and num < 76:
        int3 += 1
    elif num > 75 and num < 101:
        int4 += 1
    elif num < 0 or num > 100:
        print("Programa terminando!")

print(f"Resultados:\n Intervalo [0-25]: {int1} \n Intervalo [26-50]: {int2} \n Intervalo [51-75]: {int3} \n Intervalo [76-100]: {int4} \n  ")

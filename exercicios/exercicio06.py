# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

qntNumPares = 0
qntNumImpares = 0

for i in range(1,11):
    num = int(input(f"Digite o {i}º numero inteiro: "))
    if num % 2 == 0:
       qntNumPares += 1
    else:
        qntNumImpares += 1

print(f"Dos 10 numeros colocados, {qntNumPares} eram pares e {qntNumImpares} eram impares")
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

totalNota = 0

for i in range(1,5):
    nota = float(input(f"Insira a sua nota {i}: "))
    totalNota = totalNota + nota

media = totalNota / 4

print(f"A media é {media}")
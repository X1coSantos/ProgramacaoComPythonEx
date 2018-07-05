num_alunos = 3
nomes = []
notas = []
totalNotas = 0
maiorNota = 0
menorNota = 20

for i in range(0,num_alunos):
    nome = input("Digite o seu nome: ")
    nota = float(input("Digite a sua nota: "))
    nomes.append(nome)
    notas.append(nota)
    print("\n")
    totalNotas += nota
    if nota > maiorNota:
        maiorNota = nota
    if nota < menorNota:
        menorNota = nota

media = totalNotas / num_alunos

print(list(nomes))
print(list(notas))

j = 0
while j < len(nomes):
    print(f"Nome: {nomes[j]} | Nota: {notas[j]}")
    j += 1

for k in range(0, len(nomes)):
    print(f"{nomes[k]} - {notas[k]} ")

print(nomes[1:2])

print(f"Media: {media} \nMaior Nota: {maiorNota}\n Menor Nota: {menorNota}")
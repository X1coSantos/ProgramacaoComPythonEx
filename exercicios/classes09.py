class Pai:
    nome = "Carlos"
    sobrenome = "Santos"
    residencia = "Outeiro da Comenda"

class Filha(Pai):
    nome = "Luciana"
    olhos = "Castanhos"

class Neta(Filha):
    nome = "Maria"

print(Pai.nome, Filha.nome, Neta.nome )
print(Pai.residencia, Filha.residencia, Neta.residencia)
print(Pai.sobrenome, Filha.sobrenome, Neta.sobrenome)
print(Filha.olhos)

print(Neta.__bases__)
print(Filha.__bases__)
print(Pai.__bases__)


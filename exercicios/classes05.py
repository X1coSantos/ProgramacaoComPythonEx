from random import random

class sprites:
    def __init__(self, nome, tamanho = "grande", cor = "amarelo", arestas = "5"):
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.arestas = arestas

    def update_position(self):
        self.position = random()*10, random()*10
        print(f"{self.nome} esta agora em ({self.position})")


s1 = sprites("Nome1",cor="amarel2o",arestas=9)
print(s1.nome, s1.tamanho, s1.cor, s1.arestas)

s2 = sprites("Start2", arestas=5, cor="azul")
print(s2.nome, s2.tamanho, s2.cor, s2.arestas)

s1.update_position()
print(s1.position)

s2.update_position()
print(s2.position)

s1.update_position()
print(s1.position)

s2.update_position()
print(s2.position)

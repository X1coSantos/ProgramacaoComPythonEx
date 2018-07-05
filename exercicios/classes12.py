class Cao:
    def __init__(self, nome):
        self.nome = nome
        self.habilidades = []

    def adicionarHabilidade(self, habilidade):
        self.habilidades.append(habilidade)


cao = Cao("Cookie")
cao.adicionarHabilidade("Buscar a bola")
cao.adicionarHabilidade("Buscar o osso")

print(cao.habilidades)
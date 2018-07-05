class Inventario:
    def __init__(self):
        self.items = []

    def adicionarItem(self, nome, quantidade = 0):
        for i in range(0, quantidade):
            self.items.append(nome)

personagem1 = Inventario()
personagem1.adicionarItem("Poção de vida", 5)
personagem1.adicionarItem("Poção de mana", 3)

print(personagem1.items)

class Bola:
    def __init__(self, circunferencia = 0, cor = "", material = "tecido"):
        self.circunferencia = circunferencia
        self.cor            = cor
        self.material       = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor

bola1 = Bola(5, "Amarela", "Borracha")
print(bola1.mostraCor())
bola1.trocaCor("Vermelho")
print(bola1.mostraCor())
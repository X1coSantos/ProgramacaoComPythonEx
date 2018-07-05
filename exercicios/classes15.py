class Quadrado:
    def __init__(self, tamanhoLado = 0):
        self.tamanhoLado = tamanhoLado

    def mudarLado(self, novoLado):
        self.tamanhoLado = novoLado
        self.msg = f"\nO novo lado do qaudrado é {self.tamanhoLado}\n"
        return self.msg

    def lado(self):
        return self.tamanhoLado

    def areaQuadrado(self):
        self.area = self.tamanhoLado * self.tamanhoLado
        return self.area

quadrado1 = Quadrado()
print(quadrado1.lado(), quadrado1.mudarLado(5), quadrado1.lado(), quadrado1.areaQuadrado() )
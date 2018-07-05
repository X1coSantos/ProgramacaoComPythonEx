class CalcularNumerosComplexos:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def adicao(self):
        self.numerosReais = self.a + self.c
        self.numerosComplexos = self.b + self.d
        self.resultado = f"({self.numerosReais} + {self.numerosComplexos}i)"
        return self.resultado

    def subtracao(self):
        self.numerosReais = self.a - self.c
        self.numerosComplexos = self.b - self.d
        self.resultado = f"({self.numerosReais} + {self.numerosComplexos}i)"
        return self.resultado

    def multiplicacao(self):
        self.numerosReais = ((self.a * self.c) - (self.b * self.d))
        self.numerosComplexos = ((self.a * self.d) + (self.b * self.c))
        self.resultado = f"({self.numerosReais} + {self.numerosComplexos}i)"
        return self.resultado

    def divisao(self):
        self.numerosReais = ((self.a * self.c + self.b * self.d) / ((self.c)**2 + (self.d)**2))
        self.numerosComplexos = ((self.b * self.c - self.a * self.d) / ((self.c)**2 + (self.d)**2))
        self.resultado = f"({self.numerosReais} + {self.numerosComplexos}i)"
        return self.resultado

a = int(input("Insira o seu (a) "))
b = int(input("Insira o seu (b) "))
c = int(input("Insira o seu (c) "))
d = int(input("Insira o seu (d) "))

soma = CalcularNumerosComplexos(a, b, c, d)
resultadoSoma = soma.adicao()
resultadoSubracao = soma.subtracao()
resultadoMultiplicacao = soma.multiplicacao()
resultadoDivisao = soma.divisao()

print(resultadoSoma, resultadoSubracao, resultadoMultiplicacao, resultadoDivisao)
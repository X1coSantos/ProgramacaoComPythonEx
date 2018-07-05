# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.


class Retangulo:
    def __init__(self, nome, comprimento = 0, largura=0):
        self.nome = nome
        self.comprimento = comprimento
        self.largura = largura

    def definirLados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        self.msg = f"Lados alterados com sucesso![Largura: {self.largura} - Comprimento: {self.comprimento} ]"
        return self.msg

    def valorLados(self):
        self.msg = f"Largura: {self.largura}\n Comprimento: {self.comprimento}"
        return self.msg

    def calcularArea(self):
        self.area = self.comprimento * self.largura
        self.msg = f"A área do retangulo é {self.area}"
        return self.msg

    def calcularPerimetro(self):
        self.perimetro = self.comprimento * 2 + self.largura * 2
        self.msg = f"O perimetro do retangulo é {self.perimetro}"
        return self.msg

class Local(Retangulo):
    def __init__(self, pisos):
        self.pisos = pisos

print("Defina um triangulo")
nome = input("Digite um nome para o triangulo\n")
largura = float(input("Digite um valor para a largura\n"))
comprimento = float(input("Digite um valor par o comprimento\n"))

retangulo = Retangulo(nome)
print(retangulo.definirLados(comprimento, largura))
print(retangulo.valorLados())
print(retangulo.calcularArea())
print(retangulo.calcularPerimetro())

pisos = int(input("Informe a quantidade de pisos que pretende criar"))
construcao = Local(10)
print(construcao.nome)
print(construcao.largura)
print(construcao.comprimento)

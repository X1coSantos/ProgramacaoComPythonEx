class Op_basicas:
    def __init__(self, entrada):
        self.valor = entrada

    def __add__(self, other):
        return self.valor + other.valor

    def __mul__(self, other):
        return self.valor * other.valor

    def __call__(self, qualquerCoisa):
        return qualquerCoisa

    def __str__(self):
        return f"Ola a todos, teste do str{__class__}"

a = Op_basicas(10)
b = Op_basicas(20)
print(a * b)

c = Op_basicas("Zero -")
d = Op_basicas(5)
print(c * d)

class Op_avancadas(Op_basicas):
    def __init__(self, entrada):
        self.valor = entrada

    def __sub__(self, other):
        return self.valor - other.valor

e = Op_avancadas(10)
f = Op_avancadas(5)
print(e - f)
print(e + a)

class Op_extras(Op_avancadas):
    def quadrado(self):
        return self.valor * self.valor
    def triangulo(self, altura):
        return self.valor * altura / 2

g = Op_extras(5)
areaQuadrado = g.quadrado()
areaTriangulo = g.triangulo(5)

print(areaQuadrado)
print(areaTriangulo)

teste = Op_basicas(56)
print(teste)

teste2 = Op_extras(19)
print(teste2.valor)
print(teste2)


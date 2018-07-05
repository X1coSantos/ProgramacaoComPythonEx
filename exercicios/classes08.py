class condutoresTermicos:
    def __init__(self, nome = "Sem nome"):
        self.temperaturaFusao = 100
        self.nome = nome

class ferrosos(condutoresTermicos):
    def __init__(self):
        self.qntFerro = 45

class ducteis(ferrosos):
    def __init__(self):
        self.ductilidade = 54

a = condutoresTermicos()
print(a.nome)
print(a.temperaturaFusao)

b = condutoresTermicos("Ouro")
print(b.nome)
print(b.temperaturaFusao)

c = ferrosos()
ferrosos.nome = "teste"
print(c.nome)

d = ducteis()
ducteis.qntFerro = 4
print(d.qntFerro)
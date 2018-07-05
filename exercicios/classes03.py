class circulos:
    raio = 25.4

    def calcula_Area(self):
        self.area = 3.14*(self.raio**2)

    def calcula_Volume(self, altura):
        self.volume = 3.14*(self.raio**2)*altura


c1 = circulos()

print(dir(c1))
print(c1.raio)

c1.calcula_Area()
print(dir(c1))
print(c1.area)

c1.calcula_Volume(20)

print(c1.volume)

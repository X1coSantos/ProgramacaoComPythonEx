class Racional:
    def __init__(self, numerador, denominador = 1):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __mul__(self, outro):
        if isinstance(outro, int):
            outro = Racional(outro) # Denominador automaticamente fica 1
        novo_numerador = self.numerador * outro.numerador
        novo_denominador = self.denominador * outro.denominador
        return Racional(novo_numerador, novo_denominador)

if __name__ == "__main__":
    frac_1 = Racional(6, 4)
    frac_2 = Racional(3, 5)
    frac_3 = frac_1 * frac_2
    print(frac_1)
    print(frac_2)
    print(frac_3)

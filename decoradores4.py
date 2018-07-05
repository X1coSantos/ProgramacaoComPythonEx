def meu_decorador(funcao):
    def interior():
        print("ALGO ANTES")
        funcao()
        print("ALGO DEPOIS")
    return interior


def random_funcao():
    print("wheel")


random_funcao = meu_decorador(random_funcao)

#random_funcao()


def meu_decorador2(funcao):

    def interior():

        num = 10
        if num == 10:
            print("10")
        else:
            print("NAOOOO")

        funcao()

        print("ALGO ACONTECE DEPOUS DE FUNCAO() SER CHAMADA")
    return interior

def funcao_random2():
    print("RANDOM")

funcao_random2 = meu_decorador2(funcao_random2)

funcao_random2()
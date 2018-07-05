import time

def funcao_tempo(funcao):
    def interior(n):
        t1 = time.time()
        funcao(n)
        t2 = time.time()
        return f"Tempo para dar run nisto: {t2 - t1}"
    return interior


@funcao_tempo
def minha_funcao(n):
    num_lista = []
    for num in range(0,n):
        num_lista.append(num)
    print(f"SOMA DE TODOS {sum(num_lista)}")

print(minha_funcao(1))
print(minha_funcao(10))
print(minha_funcao(100))
print(minha_funcao(1000))


import sys

def tamanhos(n):
    """ Para verificar como as listas estão implementadas """
    dados = []
    for conta in range(n):
        x = len(dados)
        y = sys.getsizeof(dados)
        print(f"Comprimento: {x} - Tamanho - {y}")
        dados.append(conta)

tamanhos(100000)

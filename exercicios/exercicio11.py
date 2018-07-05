# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu
# argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def posOuNeg(num):
    if (type(num) == int):
        if num <= 0:
            estado = "N"
        else:
            estado = "P"
    else:
        estado = "Erro"
    return estado

num2 = posOuNeg(-150)
print(num2)
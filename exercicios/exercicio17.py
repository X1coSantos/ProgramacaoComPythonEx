num_certo = float(input("Digite o numero"))
num = 0

while(num_certo != num):
    num = float(input("Acerte:"))
    if(num > num_certo):
        resultado = "Muito alto"
    elif(num < num_certo):
        resultado = "Muito baixo"
    else:
        resultado = "Acertou"

    print(resultado)
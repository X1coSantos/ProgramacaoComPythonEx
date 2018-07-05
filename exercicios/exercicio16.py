soma, produto = 0, 1
num = float(input("Escreva um numero"))

while (num > 0 ):
    num = float(input("Escreva um numero"))
    if (num % 2 == 0):
        soma += num
    else:
        produto *= num

    print(f"Soma atual: {soma}\n Produto atual: {produto}")
else:
    print("Terminado")
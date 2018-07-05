precoTotal = 0
for i in range(1,16):
    preco = float(input("Escreva o preçod a maquina"))
    precoTotal += preco

media = precoTotal / 15

print(f"A media é {media}")

a = [1,2,3,4,5]
b = range(1,11)
c = ["Teste", 2, 6, "asdasd", [1,2,3]]
d = range(1, 100, 5)
vocabulario = ["arma", "cavalo", "tabela"]
numero = [12, 71263, 123]
vazio = []
numeros = range(1,100)

print(a,list(b),list(c), list(d))
print(vocabulario[1], vocabulario[0])
print(numero[0], numero[1])
print(numeros[-1], numeros[-2])
sep = "="*50
print(sep)

cavaleiro = ["capacete", "armadura", "botas", "luvas", "meias", "canças", "correntes", "comida"]
i = 0

while i < len(cavaleiro):
    print(cavaleiro[i])
    i += 1
print(sep)
for variavel in cavaleiro:
    print(variavel)

print(sep)

for fruta in ["laranja", "maça", "pera", "banana"]:
    print(fruta)

print(sep)

a = [1,2,3]
b = [1,3,2]
c = a + b

print(c)

print(sep)

a = [0] * 4
b = [1, 2]
c = a * 2
d = b + c

print(d)

print(sep)


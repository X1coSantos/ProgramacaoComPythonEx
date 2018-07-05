class cachoros:
    pass

a = cachoros()
b = cachoros

print(dir(a))

def nome_do_objeto(c):
    try:
        print(f"Nome: {c.__class__}, id: {id(c)}")
    except:
        print("N tem")

ndo = nome_do_objeto

ndo(b)
ndo(ndo)
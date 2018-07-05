def div(x, y):
    return x / y

#try:
    #print(div(0, 0))
#except:
    #print("Nao deu\n\n")


# f(x) | x + 2
r = (lambda x: x + 2)(2)

#print(r, end="\n\n")

soma_2 = (lambda x: x + 2)
#print(soma_2(3))


#print(list(map(lambda x: x ** 2, [1,2,3])))

from pdb import set_trace

var = 7

def func():
    global var
    print(f"1º {var}")
    var = 5
    print(f"2º {var}")


func()
print(f"3º {var}")


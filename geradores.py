l = [x*x for x in [1,2,3]]
print(l)

e = (x*x for x in [1,2,3])
#print(next(e))
#print(next(e))
#print(next(e))

for i in l:
    print(f"L -> {i}")

for a in e:
    print(f"E -> {a}")

for c in [x*x for x in [1,2,3]]:
    print(c)

for d in [x*x for x in [4,5,6]]:
    print(d)

print(list(x*x for x in [10,20,30]))

print(list([x for x in range(31) if x % 3 == 0]))

print(list((x for x in range(20) if x % 2 == 1)))

print(list((x * 2) + (x** 2) for x in range(100)))

print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

#if __name__ == '__main__':
#    fib = fibonacci()
#    print(next(fib))
#    print([next(fib) for i in range(10)])


def gera_cubos(n):
    for i in range(1, n):
        yield i ** 3

gc = gera_cubos(10)
for cubo in gc:
    print(cubo)

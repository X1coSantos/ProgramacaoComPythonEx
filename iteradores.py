for elem in [1,2,3]:
    print(elem, end=" ")

print("\n")

for elem in (1,2,3):
    print(elem, end=" ")

print("\n")

for elem in {1, 2, 3}:
    print(elem, end=" ")

print("\n")

for ch in {1:'a', 2:'b', 3:'c'}:
    print(ch, end=" ")

print("\n")

for ch in {1:'a', 2:'b', 3:'c'}.values():
    print(ch, end=" ")

print("\n")

z = zip((2,3,4),('a', 'b', 'c'))
print(z)

print(next(z))
print(next(z))
print(next(z))

print("\n")

e = enumerate("Python")
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))


print("\n")

i = iter([1,2,3])
print(next(i))
print(next(i))
print(next(i))

print("\n")

i = iter((5,4,3))
print(next(i))
print(next(i))
print(next(i))

print("\n")

c = iter("mnb")
print(next(c))
print(next(c))
print(next(c))

print("\n")

d = iter({3:'a', 2:'b', 7:'c'})
print(next(d))
print(next(d))
print(next(d))

print("\n")

r = iter(range(4))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

print("\n")

l = iter([1,2,3])
while True:
    try:
        e = next(l)
        print(e)
    except StopIteration:
        break


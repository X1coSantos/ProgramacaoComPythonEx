import itertools

iter_1 = itertools.count(3)
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))

print("\n")

iter_2 = itertools.cycle([1,2,3])
print(next(iter_2))
print(next(iter_2))
print(next(iter_2))
print(next(iter_2))
print(next(iter_2))
def tracer(func):
    def wrapper(x):
        print(func.__name__, f"({x}) = ", end=" ")
        return func(x)
    return wrapper

@tracer
def cube(x):
    return x ** 3

if __name__ == '__main__':
    print(cube(2))
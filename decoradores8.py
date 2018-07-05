from time import sleep

def sleep_decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def soma(x, y):
    return x + y

print(soma(2,2))
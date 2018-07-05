class A(object):
    @classmethod
    def foo(self):
        print(self.__name__)

    @staticmethod
    def bar():
        print("Nao tenho uso ehehe")


def funciona(f):
    def decorada(*args, **kwargs):
        print("Funciona")
        return f(*args, **kwargs)
    return decorada

@funciona
def f1():
    print("f1 aqui")

@funciona
def f2():
    print("f2 aqui")

@funciona
def f3():
    print("f3 aqui")

f1()
f2()
f3()
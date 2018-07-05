class EmptyStack(Exception):
    """ Tentativa de aceder a uma pilha vazia """
    pass

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, object):
        self.stack.append(object)

    def pop(self):
        if self.is_empty():
            raise EmptyStack("ERRO: ACESSO E MODIFIZAÇÃO DE UMA PILHA VAZIA")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise EmptyStack("ERRO: CONSULTA DE UMA PILHA VAZIA ")
        else: return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


def parent_equilib(exp):
    pilha = Stack()
    for ch in exp:
        if ch == "(" or ch == "[" or ch == "{":
            pilha.push(ch)
        elif ch == ")" or ch == "]" or ch == "}":
            if pilha.is_empty():
                return False
            else:
                topo = emparelhado(ch, pilha.top())
                return False
        else:
            pass
    return pilha.is_empty()


def emparelhado(ch1, ch2):
    return (ch1 == ")" and ch2 == "(") or (ch1 == "]" and ch2 == "[") or (ch1 == "}" and ch2 == "{")

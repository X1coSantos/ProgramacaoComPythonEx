class EmptyQueue(Exception):
    pass

class Queue:
    """
        Lista -> Os primeiros inseridos sao os primeiros a ser retirados
    """
    def __init__(self):
        self.items = []

    def insere(self, item):
        self.items.insert(0, item)

    def retira(self):
        if self.items == []:
            raise EmptyQueue(" ERRO A MODIFICAR QUEUE. NAO TEM NADA NA FILA!")
        else:
            return self.items.pop(0)

    def len(self):
        return self.items.__len__()

    def is_empty(self):
        return self.items == []

    def __str__(self):
        saida = ""
        for elem in self.items:
            saida += elem + ", "
        return ">[" + saida + "]>"

a = Queue()
a.insere("teste")
a.insere("teste1")
a.insere("teste2")
print(a)

a.retira()
print(a)

a.retira()
print(a)
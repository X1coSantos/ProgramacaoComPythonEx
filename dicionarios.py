import turtle
from random import *

def zip_teste():
    dic = zip([1,2,3], ['a', 'b', 'c'])
    return dic

dict(zip_teste())

def zip_testeV2(lista1, lista2):
    for elem in zip(lista1, lista2):
        print(elem)

lista1 = [1,2,3]
lista2 = [3,4,5]
# zip_testeV2(lista1, lista2)


list(zip(lista1, lista2))


def Dicionarios():
    """ Dicionarios """
    pass

def palavra_chave(user, password):
    """ Verifica a pass de um user """
    codigos = {"dam98" : "dam98dam98", "dam99" : "dam99dam99"}

    if user not in codigos:
        return "Não o conheço"

    pass_user = codigos[user]
    if password == pass_user:
        return "Bem vindo"
    else:
        return "Dados errados"

palavra_chave("dam98d", "dam98dam98")


def equivocos_add_palavra_triv(indice, palavra, pagina):
    """ Equivocos """
    if palavra in indice:
        indice[palavra].append(pagina)
    else:
        indice[palavra] = pagina


def listas(lista):
    """ Exercicios de listas """
    def mostra_idades():
        """ Mostra as idades """
        for idade in lista:
            print(idade)

    def mostra_idades_inversa():
        """ Mostra as idades de forma inversa """
        for i in range(len(lista) - 1, -1, -1):
            print(lista[i])

    def mostra_tudo_menos_primeira_ultima():
        """ Mostra todas as idades menos a primeira e a ultima """
        for i in range(1, len(lista) - 1):
            print(lista[i])

    def maior_menor_idade():
        """ Mostra a maior e menor idade """
        print(max(lista))
        print(min(lista))

    def soma_lista():
        """ Soma as idades da lista """
        soma = 0
        for idade in lista:
            soma += idade
        print(soma)

    def valores_inferiores(num):
        """ Calcula e mostra os valores inferiores a num """
        soma = 0
        for idade in lista:
            if idade < num:
                soma += idade
        print(soma)

    def aluno_17_anos():
        """ Verifica se existe algum aluno com 17 anos """
        idd = 17
        existe = False
        for idade in lista:
            if idade == idd:
                existe = True
        return existe

listas([1,2,6,2,3,9,6])


def soma_pares_impares_lista(lista):
    """ Mostra a soma dos pares e dos impares dentro de uma lista """
    somas = [0,0]
    for idade in lista:
        if idade % 2 == 0:
            somas[0] += idade
        else:
            somas[1] += idade
    return somas

soma_pares_impares_lista([1,4,7,9,3,2,8,5,6])


def alterna_entre_listas(lista1, lista2):
    """ Cria uma terceira lista alternando entre a lista1 e a lista 2 """
    lista = []
    for i in range(len(lista1)):
        lista.append(lista1[i])
        lista.append(lista2[i])
    return lista

alterna_entre_listas([1,2,3], [5,6,7])


def soma_cumulativa(lista):
    """
        Retorna uma nova lista em que o elemento de ordem i é a soma dos primeiros i + 1 elementos da lista
        original
        [1,2,3] = [1,3,6]
    """
    n_lista = []
    for i in range(len(lista)):
        soma = 0
        for j in range(i+1):
            soma += lista[j]
        n_lista.append(soma)
    return n_lista

soma_cumulativa([1,2,3,4])


def converte_imagem(img):
    """
        Converte imagem a preto e branco para o seu oposto
        preto -> 1
        branco -> 0
    """
    def mostra_img():
        """ Mostra a imagem """
        for i in img:
            print(i)

    def inverte_img():
        """ Inverte a imagem """
        for i in img:
            for j in range(len(i)):
                if i[j] == 0: i[j] = 1
                else: i[j] = 0

    # mostra_img()
    # inverte_img()
    # mostra_img()

converte_imagem([[0,1,0],[1,1,1],[0,1,0]])


def main_tarta(n):
    t = turtle.Turtle()

    def gera_comandos(n):
        """
            Gera comandos
            E - esquerda
            D - direita
            A - avança
            R - recua
        """
        comandos = []
        direcoes = ["E", "D", "A", "R"]
        for i in range(n):
            ran = randint(0,len(direcoes) - 1)
            comandos.append(direcoes[ran])

        return comandos


    def navega(comandos, t):
        """ Navega de acordo com os comandos """
        t.dot(10, "black")
        for comando in comandos:
            if comando == "E": t.left(90)
            if comando == "D": t.right(90)
            if comando == "A": t.forward(90)
            if comando == "R": t.backward(90)
        t.dot(10, "gray")

    comandos = gera_comandos(n)
    navega(comandos, t)
    turtle.Screen().exitonclick()

#main_tarta(10)


def loja_frutas(frutas, quantidades):
    """
        Temos 2 listas, uma com nomes das frutas outra com quantidades em kilos, queremos criar um dicionario
        com isso.
        frutas = ['maça', 'pera', 'banana']
        qnt_fr = [10,20,30]
        res = {'maça':10,'pera':20, 'banana'}
    """
    return dict(zip(frutas, quantidades))

loja_frutas(['maça', 'pera', 'banana'], [10,20,30])


def loja_frutas_eficiente(loja):
    """
        Esquema da loja:
            Fruta:
            r   - vendidos
            r   - preço por unidade
            g   - quantidade em stock
            g   - preço de venda por unidade
        loja = {'maça' : [10,2,150,1], 'banana' : [50,5,70,3], 'pera' : [20,4,50,2]}
    """

    def informacoes():
        """ Mostra as informações das frutas da loja """
        for i, c in loja.items():
            print(f"Fruta: {i}")
            print(f"Vendidos: {c[0]}")
            print(f"Preço dos vendidos: {c[1]}")
            print(f"Stock: {c[2]}")
            print(f"Comprado por: {c[3]}\n\n")

    def lucro():
        """
            Obtem o lucro
            lucro = vendidos * preço por unidade - quantidade em stock * preço de venda
        """
        lucro = 0
        for c in loja.values():
            lucro += c[0] * c[1] - c[2] * c[3]

        return lucro

    def fruta_mais_cara():
        """ Determina a fruta mais cara """
        frutaMcara = 0
        frutaMcaraNome = ""
        for i, c in loja.items():
            if c[1] > frutaMcara:
                frutaMcara = c[1]
                frutaMcaraNome = i

        print(f"A fruta mais cara é {frutaMcaraNome}, custa {frutaMcara}")


    informacoes()
    lucro()
    fruta_mais_cara()

#loja_frutas_eficiente({'maça' : [10,8,150,1], 'banana' : [50,5,70,3], 'pera' : [20,4,50,2]})



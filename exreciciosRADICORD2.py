#ALMOST THERE: Given an integer n, return True if n is within 10 of
# either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number

# n
#
# 90 e 110
#
# 190 e 210
#
def almost_there(n):
    if n >= 90 and n <= 110:
        return True
    elif n >= 190 and n <= 210:
        return True
    else: return False

#print(almost_there(100))
#print(almost_there(130))
#print(almost_there(192))
#print(almost_there(210))
#print(almost_there(23))

def almost_there2(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#FIND 33:
#Given a list of ints, return True if the array contains
#  a 3 next to a 3 somewhere.

#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def has_33(lista):
    obj = [3,3]
    tam_lista = len(lista)
    existe = False
    for i in range(tam_lista - 1):
        if obj == [lista[i],lista[i+1]]:
            existe = True
    if existe: return True
    else: return False

def teste():
    lista = [1,2,3,3,4,5,6]

    for i in range(0, len(lista) - 1, 1):
        print(i)

        print(lista[1:1+2])
        if lista[i:i+2] == [3,3]:
            print("True")

        input()

#has_33([1,2,3,3,4,2,3,3])


def paper_dol(string):
    pass

#print(paper_dol("Ola"))


def paper_doll2(string):
    resultado = ""
    for char in string:
       resultado += char * 3
    return resultado

# paper_doll2("asd")


#BLACKJACK: Given three integers between 1 and 11, if their sum is less than
#  or equal to 21, return their sum. If their sum exceeds 21 and there's an
# eleven, reduce the total sum by 10. Finally, if the sum
# (even after adjustment) exceeds 21, return 'BUST'
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(lista):
    # Se ativa estiver verdadeira, faz contagem
    # senao, nao faz
    ativa = True
    soma = 0
    for i in lista:
        if i == 6: ativa = False
        if ativa:
            soma += i
        if i == 9: ativa = True

    return soma

#print(summer_69([4, 5, 6, 7, 8, 9]))

#SPY GAME: Write a function that takes in a list of integers and returns True
# if it contains 007 in order
# lista = []
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(lista):
    obj = [0, 0, 7]
    for i in lista:
        if i == obj[0]:
            obj.remove(i)
        if obj == []: return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

def animal_crackers2(text):
    string = text.split()
    if string[0][0] == string[1][0]:
        return True
    else:
        return False

# print(animal_crackers("Duas Dalavras")

def animal_crackers(text):
    string = text.split()
    first_letter = string[0][0]
    first_letter2 = string[1][0]
    if first_letter == first_letter2:
        return True
    else:
        return False

# animal_crackers("ASD ASD")


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b: return a
        else: return b
    else:
        if a > b: return a
        else: return b

#print(lesser_of_two_evens(10,20))
#print(lesser_of_two_evens(11,20))

# MAKES TWENTY: Given two integers, return True if the sum of the integers
#  is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(a, b):
    if a == 20 or b == 20:
        return True
    else:
        if a + b == 20:
            return True
        else:
            return False

# print(makes_twenty(10,20))
# print(makes_twenty(10,10))
# print(makes_twenty(10,9))



def soma(a, b):
    return a+b

a = soma(2,2)
b = a * 4


# OLD MACDONALD: Write a function that capitalizes the first and fourth
# letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald

def old_macdownlad(text):
    return text[0:1].upper() + text[1:3] + text[3:4].upper() + text[4:]

string = "macdonald"
print(string[0:1].upper())
print(string[1:3])
print(string[3:4].upper())
print(string[4:])

print(old_macdownlad("macdonald"))

string = "macDonald"

print("\n\n\n")

lista = ["Ola", "frase", "um"]
print(" ".join(lista))
print(" ".join(lista[-1]))
frase_final = ""

lista = ["Ola", "frase", "um"]
for i in range(len(lista) - 1, -1, -1):
    frase_final += lista[i] + " "

print(frase_final)

print("\n\n\n\n")

def master_yoda(texto):
    frase = texto.split()
    frase_final = ""

    for i in range(len(frase) - 1, -1, -1):
        frase_final += frase[i] + " "

    return frase_final

print(master_yoda("Ola frase"))

def master_yoda2(texto):
    return " ".join(texto.split()[::-1])

string = "Xico"
print(string[::-1])


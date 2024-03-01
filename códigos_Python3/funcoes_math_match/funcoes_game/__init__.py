from random import randint
from funcoes_math_match.funcoes_verif import yerOrNo


def plus():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    result = num1 + num2
    answer = int(input(f'Qual o resultado de:  {num1} + {num2} = '))
    if answer != result:
        return 'w'
    else:
        return 'c'


def mmc():
    result = 1
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    answer = int(input(f'Qual o MMC (Menor múltiplo comum) entre os números {num1} e {num2}? '))
    lista1 = []
    lista2 = []
    while True:
        if num1 % 2 == 0:
            num1 /= 2
            lista1.append(2)
        elif num1 % 3 == 0:
            num1 /= 3
            lista1.append(3)
        elif num1 != 1 and num1 % num1 == 0:
            lista1.append(num1)
            num1 /= num1
        elif num1 == 1:
            lista1.append(1)
            break
    while True:
        if num2 % 2 == 0:
            num2 /= 2
            lista2.append(2)
        elif num2 % 3 == 0:
            num2 /= 3
            lista2.append(3)
        elif num2 != 1 and num2 % num2 == 0:
            lista2.append(num2)
            num2 /= num2
        elif num2 == 1:
            lista2.append(1)
            break
    if len(lista1) > len(lista2):
        comp = len(lista2)
        comp_maior = len(lista1)
        for i in range(comp):
            if lista1[i] == lista2[i]:
                result *= lista1[i]
            elif lista1[i] != lista2[i]:
                result *= (lista1[i] * lista2[i])
        comp_final = comp_maior - comp
        for i in range(comp_final):
            result *= lista1[i + comp_final]
    elif len(lista1) < len(lista2):
        comp = len(lista1)
        comp_maior = len(lista2)
        for i in range(comp):
            if lista1[i] == lista2[i]:
                result *= lista1[i]
            elif lista1[i] != lista2[i]:
                result *= (lista1[i] * lista2[i])
        for i in range(comp_maior - comp):
            result *= lista2[i+comp_maior]
    else:
        comp = len(lista1)
        for i in range(comp):
            if lista1[i] == lista2[i]:
                result *= lista1[i]
            elif lista1[i] != lista2[i]:
                result *= (lista1[i] * lista2[i])
    if answer == result:
        return 'c'
    else:
        return 'w'


def prime_number():
    num = randint(1, 100)
    answer = input(f'O número {num} é primo? ').lower()
    yerOrNo(answer)
    if num == 1:
        resp = False
    else:
        i = 1
        for c in range(1, 10):
            if num % c == 0:
                i += 1
        if i <= 2:
            resp = True
        else:
            resp = False
    if answer == 'sim' and resp:
        return 'c'
    elif answer == 'não' or answer == 'nao' and not resp:
        return 'c'
    else:
        return 'w'


def pair(num):
    if num % 2 == 0:
        return True
    else:
        return False

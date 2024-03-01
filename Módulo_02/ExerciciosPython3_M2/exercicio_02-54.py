from datetime import date

cont = 0
anoAtual = date.today().year

for i in range(0, 7):
    anoNasc = int(input('Informa a seguir, seu ano de nascimento: '))

    if anoNasc >= (anoAtual - 21):
        cont += 1

print('O número de pessoas maiores de idade é:', cont)
print('\nO número de pessoas menores de idade é:', (7 - cont))

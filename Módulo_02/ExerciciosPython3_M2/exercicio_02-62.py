termo = int(input('Informe a seguir, o primeiro termo da progressão aritmética: '))
razao = int(input('Informe agora, a razâo da progressão aritmética: '))
numTermos = 10
i = 0

while i < numTermos:
    print(termo)
    termo += razao
    i += 1
    if i == numTermos:
        i = 0
        numTermos = int(input('\nDeseja mostrar mais quantos termos da progressão aritmética? '))
        if numTermos == 0:
            print('Fim')

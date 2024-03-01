termo = int(input('Informe a seguir, o primeiro termo da progressão aritmética: '))
razao = int(input('Informe agora, a razâo da progressão aritmética: '))
i = 0

while i < 10:
    print(termo, end='')
    print(' -> 'if i != 9 else '', end='')
    termo += razao
    i += 1
print('FIM')

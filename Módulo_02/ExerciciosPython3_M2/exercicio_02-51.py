termo1 = int(input('Informe a seguir, o primeiro termo da PA: '))
razao = int(input('Informe agora, a razão da PA: '))
termo10 = termo1 + (9 * razao)

for i in range(termo1, termo10 + 1, razao):
    print(f'{i}, ', end='')
print('Fim')

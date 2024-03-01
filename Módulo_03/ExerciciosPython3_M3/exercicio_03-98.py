def contador(lst):
    if lst[0] > lst[1]:
        if lst[2] > 0:
            lst[2] = -lst[2]
        for c in range(lst[0], lst[1]-1, lst[2]):
            print(c, end=', ')
        print('Fim...\n')
    else:
        for c in range(lst[0], lst[1]+1, lst[2]):
            print(c, end=', ')
        print('Fim...\n')


cont = [1, 10, 1]
contador(cont)
cont = [10, 0, -2]
contador(cont)
cont = []
print('Informe a seguir:'
      '\n[1] - Número de início'
      '\n[2] - Número final'
      '\n[3] - Passo a passo da contagem\n')
for c in range(0, 3):
    cont.append(int(input(f'{c+1}- ')))
print('\n')
if cont[2] == 0:
    cont[2] = 1
contador(cont)

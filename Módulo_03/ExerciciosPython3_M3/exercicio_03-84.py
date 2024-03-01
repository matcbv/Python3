pessoaPeso = []
while True:
    pessoaPeso.append(input('\nInforme o nome da pessoa: ').title())
    pessoaPeso.append(float(input('Informe o peso da pessoa: ')))
    cond = input('Deseja cadastrar mais alguém? ')
    while cond not in 'SimsimNãonãoNaonao':
        print('Resposta inválida!')
        cond = input('Deseja cadastrar mais alguém? ')
    if cond in 'NãonãoNaonao':
        break
print('-' * 30)
print(f'Ao todo, foram cadastradas {len(pessoaPeso)/2:.0f} pessoas, como mostra a lista a seguir:')
for c in range(0, len(pessoaPeso), 2):
    print(f'{pessoaPeso[c]} - {pessoaPeso[c+1]}kg')
print('-' * 30)
print('Pessoas leves: ')
for c in range(0, len(pessoaPeso), 2):
    if pessoaPeso[c+1] <= 70:
        print(f'{pessoaPeso[c]} - {pessoaPeso[c+1]}kg')
print('-' * 30)
print('Pessoas pesadas: ')
for c in range(0, len(pessoaPeso), 2):
    if pessoaPeso[c+1] >= 100:
        print(f'{pessoaPeso[c]} - {pessoaPeso[c+1]}kg')
print('-' * 30)
for c in range(0, len(pessoaPeso), 2):
    if 70 < pessoaPeso[c+1] < 100:
        print(f'{pessoaPeso[c]}, com {pessoaPeso[c+1]}kg, não é nem pesado e nem leve.')

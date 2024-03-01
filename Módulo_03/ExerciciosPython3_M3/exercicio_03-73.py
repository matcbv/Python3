tabelaBr = ('Botafogo', 'Palmeiras', 'Grêmio', 'Red Bull Bragantino', 'Fluminense', 'Athletico Paranaense', 'Flamengo',
            'Fortaleza', 'Atlético Mineiro', 'São Paulo', 'Corinthians', 'Cuiabá', 'Cruzeiro', 'Internacional',
            'Vasco da Gama', 'Goiás', 'Bahia', 'Santos', 'América MG', 'Curitiba')

# Primeira forma de exibir os times:
print(f'Os cinco primeiros times são {tabelaBr[0:5]}')
# Segunda forma:
for cont in range(0, 5):
    print(f'{cont + 1}º - {tabelaBr[cont]}')
print('-' * 30)

print(f'Os seis últimos times são {tabelaBr[-4:]}')
for cont in range(1, 5):
    print(f'{21-cont}º - {tabelaBr[-cont]}')
print('-' * 30)

print(sorted(tabelaBr))
print('-' * 30)

print(f'O Chapecoente está na posição {tabelaBr.index("Flamengo") + 1}ª do Brasileirão.')

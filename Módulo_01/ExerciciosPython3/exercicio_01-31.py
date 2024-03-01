dist = int(input('Qual foi a distância, em km, percorridas na viagem: '))

if dist <= 200:
    print(f'O custo total da viagem foi: R${dist * 0.5:.2f}')
else:
    print(f'O custo total da viagem foi: R${dist * 0.45:.2f}')

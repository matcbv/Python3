vel = float(input('Informe a que velocidade o carro estava ao passar pelo radar: '))

if vel > 80:
    print(f'O veículo foi multado! A multa tem valor de {(vel - 80) * 7:.2f}')
else:
    print('O veículo não foi multado!')

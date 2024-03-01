km = int(input('Informe, a seguir, a quantidade de Km percorridos pelo carro: '))
dias = int(input('Por quantos dias o carro esteve alugado?'))

print(f'O total a se pagar pelo aluguel é: R${(dias * 60) + (km * 0.15):.2f}')

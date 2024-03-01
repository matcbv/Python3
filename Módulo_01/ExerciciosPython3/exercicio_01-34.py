salario = float(input('Digite a seguir, o salário a ser ajustado: '))

if salario > 1250:
    print(f'O novo salário desse funcionário é: R${salario * 110 / 100}')
else:
    print(f'O novo salário desse funcionário é: R%{salario * 115 / 100}')

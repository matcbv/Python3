valCasa = float(input('Informe o valor total da casa: '))
salario = float(input('Informe o salário do comprador: '))
anos = int(input('Informe, em anos, o tempo que o pagamento irá durar: '))
limiteMes = salario * 30 / 100

if valCasa / (anos * 12) > limiteMes:
    print('O empréstimo foi negado!')
else:
    print('O empréstimo foi aprovado!')

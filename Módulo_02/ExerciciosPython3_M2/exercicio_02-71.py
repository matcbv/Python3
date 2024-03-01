valorSaque = num50 = num20 = num10 = num1 = 0

while True:
    valorSaque = int(input('\nQual valor deseja sacar? R$'))

    while valorSaque - 50 >= 0:
        valorSaque -= 50
        num50 += 1
        if valorSaque == 0:
            break
    while valorSaque - 20 >= 0:
        valorSaque -= 20
        num20 += 1
        if valorSaque == 0:
            break
    while valorSaque - 10 >= 0:
        valorSaque -= 10
        num10 += 1
        if valorSaque == 0:
            break
    while valorSaque - 1 >= 0:
        valorSaque -= 1
        num1 += 1
        if valorSaque == 0:
            break

    print('\n', '=-' * 19, end='')
    print(f'''
        Notas de R$50,00 - {num50}
        Notas de R$20,00 - {num20}
        Notas de R$10,00 - {num10}
        Notas de R$1,00  - {num1}''')
    print('=-' * 19)

    novoSaque = input('\nDeseja ralizar um novo saque? ').title()
    while novoSaque not in 'SimNãoNaoSN':
        novoSaque = input('Resposta inválida. Tente novamente: ').title()
    if novoSaque in 'SimS':
        num50 = num20 = num10 = num1 = 0
    elif novoSaque in 'NãoNaoN':
        print('\nCAIXA ENCERRADO!')
        break

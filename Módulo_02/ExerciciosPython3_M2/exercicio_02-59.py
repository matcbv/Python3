print('CAUCULADORA')

num1 = int(input('Informe a seguir, o primeiro número: '))
num2 = int(input('Informe a seguir, o segundo número: '))
recomecar = ''
print('''
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa
''')

opcao = int(input('Escolha uma das opções acima: '))
if opcao < 0:
    opcao = int(input('Opção inválida! Tente novamente: '))
else:
    while opcao != 5:
        if opcao == 1:
            print('A soma dos dois números informados é:', num1 + num2)
            recomecar = input('Deseja continuar? (S / N)\n')
            if recomecar == 'S':
                opcao = 4
            else:
                opcao = int(input('Escolha uma das informadas anteriormente: '))
        elif opcao == 2:
            print('A multiplicação dos dois números informados é:', num1 * num2)
            recomecar = input('Deseja continuar? (S / N)\n')
            if recomecar == 'S':
                opcao = 4
            else:
                opcao = int(input('Escolha uma das opções informadas anteriormente: '))
        elif opcao == 3:
            if num1 > num2:
                print('O maior número entre os dois informados é o', num1)
            else:
                print('O maior número entre os dois informados é o', num2)
            recomecar = input('Deseja continuar? (S / N)\n')
            if recomecar == 'S':
                opcao = 4
            else:
                opcao = int(input('Escolha uma das opções informadas anteriormente: '))
        elif opcao == 4:
            num1 = int(input('Informe a seguir, o primeiro número: '))
            num2 = int(input('Informe a seguir, o segundo número: '))
        else:
            print('Cauculadora encerrada!')

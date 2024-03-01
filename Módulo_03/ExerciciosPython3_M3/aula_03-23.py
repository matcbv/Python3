while True:
    try:
        num1 = int(input('Informe um número qualquer: '))
        num2 = int(input('Informe um outro número qualquer: '))
        soma = num1 + num2
    except Exception as erro:
        print('Não foi possível realizar o comando acima. O erro apresentado foi:', erro.__class__)
    else:
        print(f'O resultado da some entre {num1} e {num2} é {soma}')
    finally:
        cond = input('Deseja realizar mais uma soma? [S/N]').upper()[0]
        while cond not in 'SN':
            print('Resposta inválida!')
            cond = input('Deseja realizar mais uma soma? [S/N] ').upper()[0]
        if cond == 'N':
            break

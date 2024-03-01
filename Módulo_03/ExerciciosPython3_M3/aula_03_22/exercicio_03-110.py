from pacote_ex110.dados import dadosProd
from pacote_ex110.validacao import lerDinheiro
print(f'\n{"MERCADINHO DO CERQUEIRA":-^50}')
while True:
    quantia = lerDinheiro()
    porcA = int(input('Informe a porcentagem que deseja aumentar desse valor: '))
    porcD = int(input('Informe a porcentagem que deseja diminuir desse valor: '))
    result = dadosProd(quantia, porcA, porcD)
    print()
    print(f'{"RESUMO DO VALOR"}'.center(30, '-'),
          f'\nPreço original: \t{result[0]}'
          f'\nPreço aumentado: \t{result[1]}'
          f'\nPreço diminuído: \t{result[2]}'
          f'\nPreço dobrado: \t\t{result[3]}'
          f'\nMetade do preço: \t{result[4]}'
          f'\n{"-"*30}')
    cont = input('\nDeseja visualizar as atualizações do preço de outro produto? [S/N] ').upper()[0]
    while cont not in 'SN':
        print('Resposta inválida')
        cont = input('Deseja visualizar as atualizações do preço de outro produto?')
    if cont == 'N':
        break

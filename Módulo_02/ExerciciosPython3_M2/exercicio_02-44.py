preco = float(input('Informe a seguir, o preço do produto: R$'))
formaPag = input('Deseja realizar o pagamento? Em dinheiro/cheque ou no cartão?').lower()
parcelas = 0

if formaPag == 'dinheiro/cheque':
    print(f'O valor total da compra, com o desconto, é de: R${preco * 9 / 10}')
elif formaPag == 'cartão':
    parcelas = int(input('Em quantas parcelas você deseja parcelar sua compra? (Máximo de 3 vezes)'))
    if parcelas == 1:
        print(f'O valor total da compra, com o desconto, é de: R${preco * 19 / 20}')
    elif parcelas == 2:
        print(f'O valor total da compra é de: R${preco}')
    elif parcelas == 3:
        print(f'O valor total da compra, com o juros, é de: R${preco * 12 / 10}')
    else:
        print('Forma de pagamento inválida. Tente novamente.')

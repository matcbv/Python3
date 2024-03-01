prodEprec = ('Chocolate', 5.99, 'Milkshake', 8, 'Sorvete', 10, 'Hambúrguer', 15)
print('-'*35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-'*35)
print(f'{"Nome do produto"}{"Preço":>15}')
for cont in range(0, len(prodEprec), 2):
    print(f'{prodEprec[cont]:.<25}' + f'R$ {prodEprec[cont+1]:.2f}')
print('-'*35)

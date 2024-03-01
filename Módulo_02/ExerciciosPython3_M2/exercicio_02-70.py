maiorMil = total = menorPreco = cont = 0
maisBarato = ''

while True:
    print('=-' * 25)
    nomeProd = input('Informe o nome do produto: ').title()
    preco = float(input('Informe o preço do produto acima: R$'))
    print('=-' * 25)
    cont += 1
    if preco > 1000:
        maiorMil += 1
    total += preco
    if preco < menorPreco or cont == 1:
        menorPreco = preco
        maisBarato = nomeProd
    continuar = input('Deseja adicionar outro produto? ').title()
    if continuar not in 'SimNãoNaoSN':
        continuar = input('Resposta inválida! Tente novamente:')
    elif continuar in 'NãoNaoN':
        break

print('=-' * 25)
print(f'O gasto total da compra foi de: R${total:.2f}')
print(f'Foram comprados {maiorMil} produto(s) que custam mais de R$1000,00')
print(f'O produto mais barato comprado foi o {maisBarato}, custando R${menorPreco:.2f}')
print('=-' * 25)

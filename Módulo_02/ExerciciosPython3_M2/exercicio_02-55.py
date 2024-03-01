maiorPeso = 0
menorPeso = 0

for i in range(0, 5):
    peso = float(input('Informe a seguir, o peso a ser verificado: '))
    if peso >= maiorPeso:
        maiorPeso = peso
    if peso <= menorPeso or menorPeso == 0:
        menorPeso = peso

print(f'O maior peso dentre os informados acima é {maiorPeso} e o menor {menorPeso}')

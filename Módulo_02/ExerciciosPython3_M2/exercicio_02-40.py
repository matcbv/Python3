nota1 = float(input('Informe a seguir, a primeira nota: '))
nota2 = float(input('Informe a seguir, a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('REPROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

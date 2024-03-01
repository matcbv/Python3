mais18 = numH = menos20 = 0

while True:
    print('-' * 35)
    sexo = input('Qual o sexo do indivíduo? ').title()
    idade = int(input('Qual a idade do indivíduo? '))
    print('-' * 35)

    while sexo not in 'MasculinoHomemFemininoMulher' or idade > 130:
        print('Dados inálidos! Tente novamente.')
        sexo = input('Qual o sexo do indivíduo? ').title()
        idade = int(input('Qual a idade do indivíduo? '))

    if sexo in 'HomemMasculino':
        numH += 1
    if sexo in 'MulherFeminino' and idade < 20:
        menos20 += 1
    if idade > 18:
        mais18 += 1

    continuar = input('Deseja cadastrar mais alguém?').title()
    if continuar not in 'SimNãoNaoSN':
        continuar = input('Não foi possível entender a resposta. Digite novamente: ')
    elif continuar in 'NaoNãoN':
        break

print('-' * 35)
print('O número de pessoas maiores de 18 anos cadastradas foi:', mais18)
print('O número de homens cadastrados foi:', numH)
print('O número de mulheres cadastradas com menos de 20 anos foi:', menos20)
print('-' * 35)

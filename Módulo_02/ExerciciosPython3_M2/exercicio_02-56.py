media = 0
maiorIdade = 0
maisVelho = ''
cont = 0

for i in range(0, 4):
    nome = input('Qual o seu nome? ')
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual seu sexo (M ou F)? ').upper()
    media += idade

    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido! Tente novamente.')
    else:
        if sexo == 'M' and idade > maiorIdade:
            maiorIdade = idade
            maisVelho = nome

        if sexo == 'F' and idade < 20:
            cont += 1

media = media / 4
print('\nA média de idade do grupo é', media)
print(f'O homem mais velho do grupo é o {maisVelho}, com {maiorIdade}')
print('O número de mulheres com menos de 20 anos no grupo é', cont)

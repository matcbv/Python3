from datetime import date

idade = int(input('Informe sua idade a seguir: '))
anoAtual = date.today().year
if idade > 18:
    print(f'Você passou do tempo de se alistar em {idade - 18} ano(s)')
    print(f'A date de alistamento deveria ter sido em {(anoAtual - idade) + 18}')
elif idade < 18:
    print(f'Ainda não está em tempo de se alistar, faltam {18 - idade} ano(s)')
    print(f'Você deverá se alistar em {anoAtual + (18 - idade)}')
else:
    print('Está em tempo de você se alistar!')

boletim = []
aluno = []
idAluno = 0
print('')
while True:
    aluno.append(input('\nInforma o nome do aluno a ser cauculado a média: ').title())
    aluno.append(float(input('Informe a seguir, a primeira nota do aluno: ')))
    aluno.append(float(input('Informe a seguir, a segunda nota do aluno: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    boletim.append(aluno[:])
    aluno.clear()
    cond = input('Deseja continuar adicionando alunos ao boletim? ')
    while cond not in 'SimsimNãonãoNaonao':
        print('Respota inválida!')
        cond = input('Deseja continuar adicionando alunos ao boletim? ')
    if cond in 'NãonãoNaonao':
        break
print('-' * 30)
for c in range(0, len(boletim)):
    print(f'Aluno Nº{c+1}')
    for i in range(0, len(boletim[c])):
        if i == 0:
            print(boletim[c][i], end=': ')
        elif i == len(boletim[c]) - 1:
            print(f'Média - {boletim[c][i]:.1f}')
print('-' * 30)
verNotas = input('Deseja ver quais foram as notas de algum aluno? ')
while verNotas not in 'SimsimNãonãoNaonao':
    print('Resposta inválida!')
    verNotas = input('Deseja ver quais foram as notas de algum aluno? ')
if verNotas in 'Simsim':
    idAluno = int(input('Qual o número do aluno que deseja ver as notas? '))
    if 0 > idAluno > len(boletim) - 1:
        print('Número do aluno inválido!')
        idAluno = int(input('Qual o número do aluno que deseja ver as notas? '))
print('-' * 30)
print('Nota 1: ', end='')
print(f'{boletim[idAluno-1][1]:.1f}')
print('Nota 2: ', end='')
print(f'{boletim[idAluno-1][2]:.1f}')
print('-' * 30)

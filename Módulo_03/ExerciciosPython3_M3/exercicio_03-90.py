aluno = {'nome': input('Informe o nome do aluno: ').title(), 'media': float(input('Informe a média do aluno: '))}
cond = ''

if aluno['media'] >= 7:
    cond = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    cond = 'Recuperação'
else:
    cond = 'Reprovado'

aluno['condicao'] = cond
print()
print(aluno['nome'], end=' - ')
print(f'{aluno["media"]:.2f}', end=' - ')
print(aluno['condicao'])

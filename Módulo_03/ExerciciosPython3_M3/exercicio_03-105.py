def notas(dadosAlunos, sit=False):
    result = dict()
    result['numNotas'] = len(dadosAlunos)
    result['maiorNota'] = max(dadosAlunos)
    result['menorNota'] = min(dadosAlunos)
    result['media'] = sum(dadosAlunos)/len(dadosAlunos)
    if sit:
        if result['media'] >= 8:
            result['situacao'] = 'Ótima'
        elif 6 <= result['media'] < 8:
            result['situacao'] = 'Boa'
        else:
            result['situacao'] = 'Ruim'
    return result


notasAlunos = list()
while True:
    notasAlunos.append(float(input('Informe uma nota a ser verificada: ')))
    cond = input('Deseja continuar adicionando notas? [S/N] ').upper()[0]
    while cond not in 'SN':
        print('Resposta inválida.')
        cond = input('Deseja continuar adicionando notas? [S/N] ').upper()[0]
    if cond == 'N':
        break
sit = input('Deseja verificar a situação da média da turma? [S/N] ').upper()[0]
while sit not in 'SN':
    print('Resposta inválida.')
    sit = input('Deseja verificar a situação da média da turma? [S/N] ').upper()[0]
if sit == 'S':
    result = notas(notasAlunos, sit=True)
else:
    result = notas(notasAlunos)
print()
print(result)

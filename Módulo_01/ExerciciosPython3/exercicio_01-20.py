from random import shuffle

aluno1 = input('Informe o nome do primeiro aluno a ser sorteado: ')
aluno2 = input('Informe o nome do segundo aluno a ser sorteado: ')
aluno3 = input('Informe o nome do terceiro aluno a ser sorteado: ')
aluno4 = input('Informe o nome do quarto aluno a ser sorteado: ')
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(listaAlunos)

print(f'A ordem de alunos sorteada foi: {listaAlunos}')

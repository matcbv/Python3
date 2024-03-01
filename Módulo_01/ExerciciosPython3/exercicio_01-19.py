from random import choice

aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')
listaAlunos = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno escolhido é {choice(listaAlunos)}')

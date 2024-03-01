"""Temos duas maneiras de realizar tal exercício.
A primeira envolvendo matemática e a segunda envolvendo manipulação de uma variável"""

num = int(input('Digite um número qualquer entre 0 e 9999: '))

print('\nPrimeira maneira:\n')

u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'A unidade é: {u}')
print(f'A dezena é: {d}')
print(f'A centena é: {c}')
print(f'O milhar é: {m}\n')

print('Segunda maneira:\n')

num = str(num)
print(f'A unidade é: {num[3]}')
print(f'A dezena é: {num[2]}')
print(f'A centena é: {num[1]}')
print(f'O milhar é: {num[0]}')
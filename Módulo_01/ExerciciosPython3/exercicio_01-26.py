frase = input('Digite a seguir, uma frase qualquer: ').split()
frase = ''.join(frase)

print(f'A letra a aparece', frase.count('a'), 'vezes na frase acima.')
print('A letra a aparece a primeira vez na posição', frase.find('a') + 1)
print('A letra a aparece a primeira vez na posição', frase.rfind('a') + 1)

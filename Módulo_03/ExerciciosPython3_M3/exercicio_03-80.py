numeros = []

for c in range(0, 5):
    num = int(input(f'Informe o {c + 1}ª número a ser adicionado na lista: '))
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                break
            pos += 1
print('-'*50)
print(f'A lista informada acima em ordem crescente é: ')
for pos, num in enumerate(numeros):
    print(f'{pos}º - {num}')
print('-'*50)

# Ex. 01:
dicionario = {'par' if num % 2 == 0 else 'impar': [].append(num) for num in range(10)}
# A comprehension acima não da certo, pois o método append não retorna nenhum valor, somente modifica a
# lista. Dessa forma, teremos o valor None em cada uma das chaves.
# Para executarmos a comprehension acima, devemos separá-la em duas partes e unificá-las no dicionário:
par = {num for num in range(10) if num % 2 == 0}
impar = {num for num in range(10) if num % 2 != 0}
dicionario = {'par': par, 'impar': impar}
print(dicionario)

dicionario = {
    'chave 01': 'valor01',
    'chave 02': 'valor02',
    'chave 03': 10
}
print(dicionario)
print('-'*60)
# Parecido com as listas, no dictionary comprehension devemos especificar a chave e valor, junto do
# dicionário com o método items(). Assim como na list comprehension, podemos adicionar condicionais. Ex.:

dicionario02 = {chave: valor.upper() if isinstance(valor, str) else valor for chave, valor in dicionario.items()}
print(dicionario02)
print('-'*60)
# No exemplo acima, só iremos passar os valores para maiúsculo se forem do tipo string, senão iremos passar
# o valor sem nenhuma alteração.

# Também podemos realizar set comprehensions:
conjunto = {num for num in range(10)}
# Que seria o mesmo que conjunto = set(range(10))
print(conjunto)
print('-'*60)

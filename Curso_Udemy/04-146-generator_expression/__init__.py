from sys import getsizeof

# Um generator é uma função capaz de pausar durante o decorrer da iteração.
# Obs.: Um generator é também um iterator, mas não o contrário.

# Estaremos demonstrando abaixo um exemplo do descrito acima:
# Uma lista é armazenada por inteiro na memória, enquanto o gerador gera elemento por elemento.
lista = [num for num in range(100)]
# Um gerador é criado por parênteses junto de um iterável.
gerador = (num for num in range(100))
# Podemos verificar isso verificando o espaço em bytes na memória que ambos ocupam:
print(getsizeof(lista))
print(getsizeof(gerador))
print('-' * 60)
# Dessa forma, caso nosso iterável lide com dados.txt muito extensos, talvez seja mais interessante
# trabalharmos com os geradores.
print(lista)
for num in gerador:
    print(num)

# Obs.: Não é possível acessar diretamente um gerador, pois seus elementos ainda não foram gerados. Ex.:
# gerador[0] e len(gerador) não darão certo.


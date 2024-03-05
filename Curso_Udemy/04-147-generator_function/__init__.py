# Uma generator function é caracterizada por possuir uma pausa (yield) em seu escopo.
# Um yield é responsável por retornar um valor assim como return, porém sem encerrar a função.
def generator(num=0, maximo=10):
    yield num  # Pausa
    while num < maximo:
        num += 1
        print('continuando...')
        yield num
    return 'ACABOU'


# Criando um gerador a partir de uma função geradora:
gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print('-'*60)
# Também podemos realizar as chamadas por uma estrutura de um iterador:
for n in gen:
    print(n)
# Obs.: Lembrando que independente do escopo que estiver, a chamada irá continuar da última pausa
# feita pela generator function.

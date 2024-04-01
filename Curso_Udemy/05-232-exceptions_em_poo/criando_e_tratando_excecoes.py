# Para criarmos nossas próprias exceções, devemos apenas criar uma classe, herdando por recomendação,
# a classe Exception. Por convenção, utilizamos sempre a palavra Error ao final de uma classe de
# criação de exceções.

# Podemos utilizar palavras-chave para levantarmos exceções. Essas palavras podem variar conforme
# a linguagem. Em Python utilizamos raise (levantar), mas em outras linguagens podemos ver throw (lançar).
class MyError(Exception):
    pass


# Para levantarmos uma exceção, iremos utilizar a palavra-chave raise junto de uma função.
# Obs.: Essa função só levantará uma exceção, nunca retornará nada.
def levantar():
    raise MyError('Esta é a mensagem do meu erro!')


# Para realizarmos a tratativa de nosso erro, podemos utilizar o try e except:
try:
    # Como levantar levanta um erro, sempre entraremos no except.
    levantar()
# Armazenaremos nossa mensagem de erro em um objeto e então o exibiremos na tela. Dessa forma,
# somente a mensagem será enviada.
except MyError as error:
    print(error)

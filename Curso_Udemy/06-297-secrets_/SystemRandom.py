# A classe SystemRandom utiliza um gerador de números aleatórios criptograficamente seguro fornecido pelo
# sistema operacional. Isso o torna mais adequado para ser utilizado em como geração de senhas,
# chaves de criptografia, tokens de autenticação, entre outros.
#
# A classe SystemRandom fornece os mesmos métodos que a classe random.Random para gerar números aleatórios,
# como random(), randint(), choices(), entre outros.
from secrets import SystemRandom
# Junto da propriedade string, podemos criar senhas aleatórias. Veremos como abaixo dos primeiros exemplos:
import string as s

random_ = SystemRandom()

print('randint:', random_.randint(1, 10))
print()
print('randrange:', random_.randrange(0, 10, 2))
print()
rand_float = random_.uniform(1, 10)
print(f'randfloat: {rand_float:.2f}')
print()

# Criando nossa senha:
# Obs.: Veremos mais sobre o módulo string na próxima seção
# Utilizaremos o método choices, passando elementos do nosso módulo string.
# Junto a isso, definiremos o número de caracteres que desejamos ter em nossa senha.
password = ''.join(random_.choices(s.digits + s.ascii_letters + s.punctuation, k=8))
print(password)

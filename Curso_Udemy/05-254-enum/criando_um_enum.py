# Para criarmos nossa classe tipo enum, devemos importar o módulo enum:
import enum


# Podemos criar nossa classe do tipo enum de duas maneiras. Utilizando a classe Enum diretamente:
# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(enum.Enum):
    # Substituindo os valores por enum.auto(), eles são preenchidos automaticamente seguindo uma
    # ordem crescente começando pelo 1.
    ESQUERDA = 1
    DIREITA = 2


# Para obtermos os membros, temos três opções:
# Através do valor, que por padrão, é representado por um número inteiro começando em 1:
print(Direcoes(1), Direcoes(2))
# Através da chave, representa pelo nome do respectivo elemento:
print(Direcoes['ESQUERDA'], Direcoes['DIREITA'])
# Através do acesso direto a esses membros
print(Direcoes.ESQUERDA, Direcoes.DIREITA)

# Para obtermos somente a chave de um membro, devemos utilizar a palavra-chave value ao final:
# Obs.: Iremos utilizar somente um dos três métodos acima para os exemplos restantes, porém ambos
# os três iriam funcionar da mesma maneira.
print(Direcoes.ESQUERDA.value)

# Já para obtermos somente o nome de um membro, utilizamos a palavra-chave name ao final:
print(Direcoes.DIREITA.name)
print()


def mover(direcao: Direcoes):
    # Podemos utilizar o isinstance para verificar se o valor passado é do tipo Direcoes,
    # gerando um erro caso contrário.
    if not isinstance(direcao, Direcoes):
        raise TypeError('A direção informada não é do tipo Direcoes')
    print('Você andou para', direcao.name)


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)

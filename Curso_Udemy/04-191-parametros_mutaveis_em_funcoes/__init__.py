# Ao utilizarmos parâmetros mutáveis em funções, podemos ter um problema na tratativa de nossos dados.
# Quando definimos um dos parâmetros de nossa função com um valor padrão sendo um elemento mutável
# (iteráveis, em geral), esse elemento é criado e utilizado em todas as chamadas da função. Ex.:
def adiciona_produtos(nome, lst=[]):
    lst.append(nome)
    return lst


# Ao chamarmos nossa função, será retornada a lista criada.
lista_produtos = adiciona_produtos('Papel')
print(lista_produtos)

# Chamando novamente a função, porém agora, atribuindo a lista a um novo objeto.
nova_lista_produtos = (adiciona_produtos('Caneta'))
print(nova_lista_produtos)
# Como pudemos ver, a mesma lista foi utilizada, mesmo a função chamada em momentos diferentes.
# Dessa forma, devemos criar a lista anteriormente e passá-la por parâmetro, ou utilizar o valor pré-definido none.


def nova_adiciona_produtos(nome, lst=None):
    if lst is None:
        lst = []
    lst.append(nome)
    return lst


# No caso acima, caso o valor padrão de lst seja None, estaremos criando uma função no escopo da função.
# Logo, a cada chamada, uma nova função será chamada e retornada. Ex.:
ultima_lista_produtos = nova_adiciona_produtos('Lápis')
print(ultima_lista_produtos)
ultima_lista_produtos = nova_adiciona_produtos('Borracha', ultima_lista_produtos)
print(ultima_lista_produtos)

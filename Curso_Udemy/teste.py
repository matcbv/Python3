produto = 'papel'
preco = 20
lista = []

def recebe_produtos(*prod):
    lista.append(prod)
    print(lista)


recebe_produtos(produto, preco)

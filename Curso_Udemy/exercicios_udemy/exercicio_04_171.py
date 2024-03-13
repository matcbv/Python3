def somar_listas(lst_01, lst_02):
    menor = min(len(lista_01), len(lista_02))
    soma_das_listas = [
        lst_01[i] + lst_02[i] for i in range(menor)
    ]
    return soma_das_listas


lista_01 = [1, 2, 3, 4]
lista_02 = [1, 2, 3, 4, 5, 6]

result = somar_listas(lista_01, lista_02)
print(result)

# Podemos simplificar o código acima realizando:

lista_01 = [1, 2, 3, 4]
lista_02 = [1, 2, 3, 4, 5, 6]
soma_listas = [sum(v) for v in list(zip(lista_01, lista_02))]  # ou então: v1 + v2 for v1, v2 in zip(lista_01, lista_02)
print(soma_listas)

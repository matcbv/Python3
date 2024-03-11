# def verifica_divisor(divisor):
#     soma_divisoes = 0
#     while divisor <= 0:
#         print('Divisor inválido! Informe um divisor superior a zero.')
#         divisor = int(input('Informe um divisor: '))
#
#     def divide(dividendo):
#         nonlocal soma_divisoes
#         resultado = dividendo/divisor
#         soma_divisoes += resultado
#         return resultado, soma_divisoes
#     return divide
#
#
# dividir = verifica_divisor(int(input('Informe um divisor: ')))
# result, soma = dividir(int(input('Informe um dividendo: ')))
# print(result, soma)
import os

nome_arq = 'lista_compras.txt'
with open(nome_arq, 'a+') as texto:

    print(texto.read())



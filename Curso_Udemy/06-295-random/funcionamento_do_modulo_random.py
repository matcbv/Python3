# O módulo random, por padrão, funciona através do método seed, junto do método time do módulo time.
# Random irá retornar um número pseudoaleatório com base no número obtido pelo método time.
# Obs.: Lembrando que o método time retorna o número de segundos desde 01/01/1970.
import random
from time import time
from random import seed

# Chamando o método seed, estamos inicializando o gerador de números pseudoaleatórios com o
# número passado por parâmetro, que no caso, é o número de segundo obtidos com o método time.
# Como o time muda seu valor a cada execução do programa, garantimos que as sequências não
# irão se repetir.
seed(time())

# Caso passemos um número qualquer, nosso gerador será inicializado se baseando naquele número
# em questão. Como é um número fixo, a sequência numérica gerada pelo nosso gerador será sempre
# a mesma em toda a execução. Cada número
# Obs.: A função seed utiliza números inteiros. Caso passemos um número flutuante, ele será
# automaticamente convertido para um inteiro pela função int.
seed(1)

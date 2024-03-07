# Um módulo é um executável (.py), que pode conter definições de classe, método, variáveis e um código executável.
# Um pacote é basicamente um diretório que contém um módulo __init__.py, podendo conter também outros módulos.
# Podemos importar módulos de classes de diferentes maneiras:
# import "nome_da_classe": dessa maneira, importamos todos os métodos dessa classe.
# from "nome_da_classe" import "nome do método": desse modo, importamos somente um
# método da classe em questão. Também podemos importar mais de um módulo separando-os por vírgula.
# from "nome_da_classe" import *: importamos todos os métodos dessa classe, podendo chamá-los
# diretamente sem fazer referência ao elemento pai. Ex.: time.sleep -> sleep.
# Obs.: Utilizar o * é considerada uma má-prática, podendo ter conflitos de nome em nosso código.
# as: Ao utilizarmos o as, podemos renomear um elemento, como uma classe ou método. Ex.:
import time as tempo
# ou:
from time import sleep as soneca
# Dessa maneira, teremos duas opções de chamada:
tempo.sleep(1)
soneca(1)

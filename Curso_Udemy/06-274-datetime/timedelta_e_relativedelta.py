from datetime import datetime, timedelta

# Outro fato interessante ao se trabalhar com datas, é a capacidade de
# realizarmos cáuculos com elas.

data_01 = datetime(2024, 4, 11, 1, 14, 16)
data_02 = datetime(2024, 4, 9, 13, 32, 4)
# Podemos realizar verificações como:
print(data_01 > data_02)
print(data_01 == data_02)
# Tais verificações acima irão nos retornar booleans.

# Podemos obter a diferença entre duas datas:
print(data_01 - data_02)

# Podemos obter a diferença total entre duas datas em segundos através da função total_seconds:
print((data_01-data_02).total_seconds())

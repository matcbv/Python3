# Veremos agora a classe relativedelta, do módulo relativedelta.
from datetime import datetime
from dateutil.relativedelta import relativedelta

data_01 = datetime(2024, 4, 11, 1, 14, 16)
data_02 = datetime(2024, 4, 9, 13, 32, 4)

# Com a classe relativedelta, assim como com timedelta, conseguimos realizar
# cáuculos com nossas datas. relativedelta, por sua vez, apresenta mais possibilidades
# para realizarmos nossas operações.

# Possívels valores
# year, month, day, hour, minute, second, microsecond: tais valores, quando atribuídos
# ao relativedelta, definirão valores absolutos, e irão substituir o valor original.

# years, months, days, hours, minutes, seconds, microseconds: tais valores, quando atribuídos
# ao relativedelta, definirão valores relativos, e irão somar ou subtrair do valor original.

# Com relativadelta, podemos obter a diferença entre duas datas:
diferenca_datas = relativedelta(data_01, data_02)
print()
# O resultado será uma instância da classe diferenca_datas.
# Dando print em nossa instância, um repr é exibido.
print(diferenca_datas)
# Podemos verificar somente alguns atributos dessa instância, como:
# dias, horas, minutos, segundos, etc
print(f'Diferença de dias: {diferenca_datas.days}', f'Diferença de horas: {diferenca_datas.hours}', sep='\n')
print()

# Também podemos realizar a soma entre datas:
# Somando dois anos à diferença obtida acima:
dois_anos = relativedelta(years=2)
soma_ano = diferenca_datas + dois_anos
print(soma_ano)

# Substituindo o ano de uma data qualquer:
troca_ano = relativedelta(year=2025)
data = datetime(2024, 4, 17)
soma_data = data + troca_ano
print(soma_data)

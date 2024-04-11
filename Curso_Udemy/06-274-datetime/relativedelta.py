# Veremos agora a  classe relativedelta, do módulo relativedelta.
from datetime import datetime
from dateutil.relativedelta import relativedelta

data_01 = datetime(2024, 4, 11, 1, 14, 16)
data_02 = datetime(2024, 4, 9, 13, 32, 4)

# Com a classe relativedelta, assim como com timedelta, conseguimos realizar
# cáuculos com nossas datas. relativedelta, por sua vez, apresenta mais possibilidades
# para realizarmos nossas operações.

# Com relativadelta, podemos obter a diferença entre duas datas:
diferenca_datas = (relativedelta(data_01, data_02))
# O resultado será uma instância da classe diferenca_datas.
# Dando print em nossa instância, um repr é exibido.
print(diferenca_datas)
# Podemos verificar somente alguns atributos dessa instância, como:
# dias, horas, minutos, segundos, etc
print('Diferença de dias:', diferenca_datas.days, 'Diferença de horas:', diferenca_datas.hours)

# Também podemos realizar a soma entre datas:

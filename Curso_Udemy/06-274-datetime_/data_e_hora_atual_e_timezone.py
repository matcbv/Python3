from datetime import datetime
from pytz import timezone

# Podemos obtermos a data e hora atuais de sua máquina, utilizamos a função now:
data_hora_atual = datetime.now()
print(data_hora_atual)

# Podemos passar uma timezone diferente para nossa função now. Para isso utilizaremos
# os pacotes externos chamados pytz e types-pytz. pytz adiciona diferentes timezones,
# enquanto types-pytz adiciona as tipagens de pytz para serem reconhecidas pelo Python.

# Obs.: types-putz é baixado via terminal pelo pip.

data_hora_tokyo = datetime.now(timezone('Asia/Tokyo'))
print(data_hora_tokyo)

# Também podemos utilizar timezones na criação de nossas datas:
data_com_timezone = datetime(2024, 4, 11, 00, 17, 43, tzinfo=timezone('Asia/Tokyo'))
# Dessa forma, teremos nossa data e hora, porém acrescido com a timezone ao final.
print(data_com_timezone)

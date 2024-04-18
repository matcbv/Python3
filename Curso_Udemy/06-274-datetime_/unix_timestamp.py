# Também conseguimos criar data utilizando o unix time stamp. O unix time stamp se trata do número
# de segundos passados de 01/01/1970 até o atual momento.
# Para obtermos o tempo unix atual, utilizaremos a função timestamp():
from datetime import datetime

data = datetime.now()
# Iremos chamar nossa função timestamp, que irá retornar o tempo unix da data atual obtida acima:
tempo_unix = (data.timestamp())
print(tempo_unix)
# Também podemos criar data a partir do tempo unix. No caso abaixo, irá nos retornar a data atual:
print(datetime.fromtimestamp(tempo_unix))

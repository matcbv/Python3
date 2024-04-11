from datetime import datetime

# Podemos obtermos a data e hora atuais de sua máquina, utilizamos a função now:
data_hora_atual = datetime.now()
print(data_hora_atual)

# Podemos passar uma timezone diferente para nossa função now. Para isso utilizaremos
# um pacote externo chamado pytz.
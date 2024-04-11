# Conseguimos formatar nossas datas através da classe datetime.
from datetime import datetime

# Podemos criar nossas próprias datas passando os valores para a classe datetime:
data = datetime(2024, 4, 10)
print(data)
# Também podemos estar criando nossa data com horário:
data_com_hora = datetime(2024, 4, 10, 22, 50, )
print(data_com_hora)
# Os valores que datetime aceita são: ano, mês, dia, hora, minuto, segundo, milissegundo.

# Também podemos criar nossa data através da formatação de uma string. Isso pode ser feito
# por meio da função strptime contida na classe datetime:
str_com_data = '2024/04/10 - 22:50:00'
# Para informarmos a formatação que desejamos aplicar a nossa data, devemos utilizar as diretivas.
# Veremos as principais diretivas abaixo:
# %y - Ano sem século e preenchendo com zeros. Ex: (01, ..., 99)
# %Y - Ano com século como decimal. Ex.: (0001, ..., 9999)
# %m - Mês preenchido com zeros.
# %d - Dia preenchida com zeros.
# %H - Hora em formato 24h.
# %I - Hora em formato 12h.
# %M - Minuto preenchido com zeros.
# %S - Segundo preenchido com zeros.
# %f - Microssegundo com seis dígitos, preenchido com zeros.
# Obs.: Segue o link contendo todos os detalhes da classe datetime: https://docs.python.org/3/library/datetime.html
formatacao_para_data = '%Y/%m/%d - %H:%M:%S'
data_formatada = datetime.strptime(str_com_data, formatacao_para_data)
print(data_formatada)

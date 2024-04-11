# Através do módulo calendar, conseguimos trabalhar com calendários, obtendo informações
# de dia e semana.
import calendar

# Para obtermos um calendário de um ano, utilizamos a função
print(calendar.calendar(2024))
print('-'*90)

# Podemos descobrir o índice do dia da semana e o último dia do mês, através do comando monthrange:
indice_semana, ultimo_dia_mes = calendar.monthrange(2024, 12)
# O índice dos dias da semana começam em 0, representando segunda, e vão até 6, representando domingo.
print(list(enumerate(calendar.day_name)))
print('-'*90)

# Para descobrirmos o nome do dia da semana, utilizamos o comando day_name. Por parâmetro, passamos o
# índice da semana obtido.
# Através do comando weekday, descobrimos o índice da semana que determinado dia possui.
print(calendar.day_name[calendar.weekday(2024, 12, 5)])

# Podemos também, obter o calendário de um mês em específico com a função monthcalendar.
# Tal função irá retornar uma lista contendo os dias do mês, organizados em listas que represetam
# as semanas daquele mês.
# Obs.: Os dias com valor 0 não pertencem à aquele mês.
calendario_mes = calendar.monthcalendar(2024, 12)
for dia in calendario_mes:
    print(dia)
# Os índices de cada um dos valores das listas, representarão o dia daquela respectiva semana.
# No exemplo acima, o primeiro dia do mês começa em um domingo.

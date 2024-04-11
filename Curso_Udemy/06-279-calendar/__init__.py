# Através do módulo calendar, conseguimos trabalhar com calendários, obtendo informações
# de dia e semana.
import calendar

# Para obtermos um calendário de um ano, utilizamos a função
print(calendar.calendar(2024))
print('-'*90)

# Podemos também obter o calendário de um mês em específico com a função monthcalendar:
print(calendar.monthcalendar(2024, 12))
print('-'*90)

# Podemos descobrir o índice do dia semana e o último dia do mês através do comando monthrange:
# O índice dos dias da semana começa em 0, representando a segunda, e vai até 6, representando o domingo.
print(calendar.monthrange(2024, 12))
print('-'*90)

# Através do comando weekday, descobrimos o índice da semana que determinado dia possui.
indice_semana = calendar.weekday(2024, 12, 5)
print(indice_semana)

# Para descobrirmos o nome do dia da semana, utilizamos o comando day_name. Por parâmetro, passamos o
# índice da semana obtido.
print(calendar.day_name[indice_semana])

# Podemos criar um calendár
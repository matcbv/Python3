# Através do módulo locale, conseguimos alterar a linguagem sendo utilizada em nosso módulo.
import locale
import calendar

# Com a função setlocale, podemos informar de qual elemento desejamos alterar a linguagem.
# Podemos alterar os valores numéricos (LC_NUMERIC), monetários (LC_MONEY), de tempo (LC_TIME), etc.
# No exemplo abaixo, estaremos alterando todos os valores de nosso módulo para a linguagem padrão do
# nosso sistema operacional. Isso é feito através do atributo LC_ALL como primeiro parâmetro, junto de
# uma string vazia como segundo.
locale.setlocale(locale.LC_ALL, '')
# Poderíamos também especificar uma linguagem específica junto de uma codificação para ser utilizada.

# Com a função getlocale(), conseguimos ver qual linguagem e codificação estão sendo utilizada no módulo.
print(locale.getlocale())

# Caso quisessemos utilizar a codificação UTF-8, teríamos que passar algo como:
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

# Como podemos ver abaixo, nosso calendário está em português.
print(calendar.calendar(2023))

from datetime import datetime

data_formato_padrao = datetime(2024, 4, 10, 22, 50)
formato_brasileiro = '%d-%m-%Y'
# Podemos chamar nosso método strftime de duas maneiras, chamando-o através da classe datetime:
# Obs.: Neste caso, devemos passar nosso objeto do tipo datetime, junto de uma string contendo a formatação.
# datetime.strftime(obj_datetime, 'formato')
# Ou chamando-o através da nossa instância, passando somente o formato dessa vez:
# instancia.srtftime('formato').
data_formato_brasil = data_formato_padrao.strftime(formato_brasileiro)
print(data_formato_brasil)

# Podemos utilizar somente um dos valores da data em específico, assim como vimos anteriormente:
print(data_formato_padrao.strftime('%Y'), data_formato_padrao.year)
# Chamando diretamente os atributos de nossa instância, os valores serão do tipo inteiro.
print(type(data_formato_padrao.year))

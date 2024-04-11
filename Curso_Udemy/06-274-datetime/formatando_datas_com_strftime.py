from datetime import datetime

data_01 = str(datetime(2024, 4, 10, 22, 50))
data_02 = str(datetime(2024, 4, 10, 22, 50))
formato = '%Y-%m-%d %H:%M:%S'
data_formato_padrao = datetime.strptime(data_01, formato)
formato_brasileiro = '%d-%m-%Y'
# Podemos chamar nosso datetime de duas maneiras, chamando-o através da classe datetime:
# datetime.strftime('data', 'formato')
# Ou chamando-o através da nossa instância, passando somente o formato dessa vez:
# instancia.srtftime('formato').
# Obs.: Os parâmetros devem ser do tipo string.
data_formato_brasil = data_formato_padrao.strftime(formato_brasileiro)
print(data_formato_brasil)

# Podemos utilizar somente um dos valores da data em específico, assim como vimos anteriormente:
print(data_formato_padrao.strftime('%Y'), data_formato_padrao.year)
# Chamando diretamente os atributos de nossa instância, os valores serão do tipo inteiro.
print(type(data_formato_padrao.year))

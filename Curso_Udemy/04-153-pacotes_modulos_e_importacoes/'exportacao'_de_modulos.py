# Quando importamos um método em determinado módulo, podemos falar que a importação
# também "exporta" os métodos provenientes dela. Ex.:
from diretorio_04_153_exemplo_estrutra_de_dados.pacote_para_exportacao.modulo_main import exp
print(exp)

# No exemplo acima, importamos a função retornar_msg que está contida no modulo_02 através do
# modulo_principal. Conseguimos tal feito devido ao modulo_principal também importar o modulo_02.
# Obs.: Isso só pode ser feito caso o caminho coincida com o caminho a ser feito pelo módulo atual.

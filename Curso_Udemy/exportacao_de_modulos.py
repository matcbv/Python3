# Quando importamos um método em determinado módulo, podemos falar que a importação
# também "exporta" os métodos provenientes dela. Ex.:
from exportacao_de_modulos_04_153.modulo_para_exportar import msg
print('A mensagem chegou ao destino (módulo atual).')
print(msg)
# No exemplo acima, importamos a variável msg contida no "modulo_para_importar" através do
# módulo "modulo_para_exportar". Conseguimos tal feito devido ao "modulo_para_exportar" também
# importar o "modulo_para_importar", disponibilizando os elementos dele.
# Obs.: Isso só pode ser feito caso o caminho coincida com o caminho a ser feito pelo módulo atual.

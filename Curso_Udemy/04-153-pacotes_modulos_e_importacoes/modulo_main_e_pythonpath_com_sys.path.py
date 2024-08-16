# Com o método path, conseguimos ver todos os caminhos conhecidos pelo python.
# Esses caminhos tem os módulos e pacotes contidos neles acessados pelo python e,
# consequentemente, podendo ser importados para uso. Tais módulos e pacotes são os contidos em mesmo pacote,
# ou em subpacotes. Caminhos acima disso não são conhecidos por padrão.
# Para importarmos um módulo externo a esses caminhos, devemos adicionar o caminho
# em que ele está contido na lista sys.path ou diretamente na variável de ambiente PYTHONPATH.
# Alterando a sys.path, estaremos adicionando o caminho somente para o programa em execução,
# já alterando diretamente a variável PYTHONPATH, estaremos adicionando o caminho de forma geral.
# Sempre que a lista sys.path é iniciada, consulta a variável de ambiente do Python PYTHONPATH.
# Ex.: sys.path.append("caminho_do_pacote/módulo")
import sys
print(sys.path)

# O primeiro módulo executado pelo Python chama-se main, sendo o ponto inicial do seu programa.
# Já os importados terão o nome do próprio módulo.
import modulo_secundario
print('Este módulo se chama:', __name__)
# Caso formos no modulo_secundario.py e dermos um print com __name__, veremos que se chamará main,
# pois ele será o módulo inicial daquela execução.

# Quando um módulo é importado, ele é executado automaticamente.
# Dessa maneira, o Python irá executar tudo o que for possível de imediato, como um comando print(),
# mas não uma função, por exemplo.

soma = modulo_secundario.somar(2, 3)
print(soma)

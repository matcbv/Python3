# Para obtermos informações de um módulo em Python, podemos utilizar duas funções embutidas.
# Essas são: dir e help.
import modulo_para_importar
# dir: Com a função dir, podemos ver o conteúdo contido no módulo em questão. Ele retorna
# tal conteúdo em uma lista de strings.
print(dir(modulo_para_importar))
# Podemos acessar cada um dos elementos contidos na lista de dir diretamente:
print(modulo_para_importar.__name__)
print(modulo_para_importar.__doc__)

print()
# help: Com a função help, podemos obter informações como: nome do módulo, suas funções,
# seus dados.txt e seu caminho.
help(modulo_para_importar)

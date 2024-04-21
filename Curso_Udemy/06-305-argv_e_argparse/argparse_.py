from argparse import ArgumentParser

# Criando uma instância da classe ArgumentParser:
parser = ArgumentParser()

# Passando os argumentos para os parâmetros do método add_argument:
# Obs.: Esse, é responsável por adicionar argumentos à instância de um objeto ArgumentParser.
# Ele é usado para definir quais argumentos um programa pode aceitar na linha de comando
# e como esses argumentos devem ser tratados.
parser.add_argument(
    '-s', '--show',
    # O parâmetro help indica a mensagem a ser exibida ao utilizarmos o comando de ajuda (-h, --help)
    help='Mostra "Olá mundo" na tela por padrão',
    # O parâmetro help explicita o tipo de argumento esperado pelo argumento.
    # Obs.: Por padrão, o valor definido é do tipo list.
    # type=str,
    # O parâmetro metavar é uma forma de fornecer uma mensagem informativa na mensagem
    # de ajuda, indicando qual o tipo de valor esperado para o argumento.
    metavar='STRING',
    # Com default, podemos definir um valor padrão para nosso argumento.
    default='Olá mundo',
    # Com required, podemos exigir que nosso argumento seja enviado junto a chamada do módulo.
    required=False,
    # Com action, definimos como o valor do determinado argumento deve ser tratado.
    # action='append'
    # nargs é responsável por definir o número de argumentos que nosso argumento aceitará.
    # Podemos passar um número inteiro, ou valores especiais, como:
    # '?': aceita zero ou um valor. Isso significa que o argumento pode ser omitido ou pode ter um valor associado.
    # '*': aceita zero ou um, ou mais valores. O argumento pode ser omitido completamente ou pode ter um ou mais
    # valores associados.
    # '+': aceita um ou mais valores. Isso significa que o argumento deve ter pelo menos um valor associado,
    # mas pode ter mais.
    nargs='+'
)

# Outro exemplo de argumento:
parser.add_argument(
    '-c', '--check',
    help='Exibe o status do argumento',
    # Com o valor store_true, definimos que o valor True será retornado caso o
    # argumento esteja presenta no comando.
    # Obs.: Também temos o store_false, que tem o papel oposto.
    action='store_true'
)

args = parser.parse_args()

if args.show is None:
    print('Você não passou valor algum para -s/--show.')
    print(args.show)
else:
    print('Valores do argumento:', args.show)

print(args.check)

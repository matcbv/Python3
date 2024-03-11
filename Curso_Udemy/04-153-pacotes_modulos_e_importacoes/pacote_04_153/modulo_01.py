# Sempre devemos organizar nossos projetos com um módulo principal, e nele, realizar todas as
# importações necessárias. Os métodos e classes externas devem ser armazenados em um pacote externo,
# mantendo assim, um código organizado.
from modulo_02 import *
from modulo_02 import texto

# Caso seja feita uma importação com * (all), podemos definir quais elementos serão passados
# nessa importação. Isso é feito através do atributo especial __all__.
print(retornar_msg())
print(numero)
# Caso tentemos chamar a variável "texto" presente no módulo_02, ela não será encontrada, pois
# não foi passada junto do atributo __all__.

# Ao importamos ele diretamente, temos acesso normalmente.
print(texto)

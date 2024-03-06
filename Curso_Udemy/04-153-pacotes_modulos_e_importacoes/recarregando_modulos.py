# Um módulo, quando importado, não consegue ser importado novamente. Porém, podemos realizar o
# recarregamento daquele módulo. Conseguimos realizar tal procedimento através do módulo importlib. Ex.:
import modulo
import importlib

importlib.reload(modulo)
# Dessa maneira, nosso módulo será recarregado. Lembrando que isso não é feito a menos que façamos
# tal requisição.

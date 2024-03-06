# Else: Irá ser executado caso nenhuma exceção seja retornada.
# Finally: Sempre será executado, independendo de retornar ou não uma exceção.
from time import sleep

try:
    print('Verificando se irá retornar algum exceção...')
    sleep(1)
except Exception:
    print('Retornou uma exceção!')
else:
    print('Nenhuma exceção retornada, está tudo certo!')
finally:
    print('Verificação encerrada!')

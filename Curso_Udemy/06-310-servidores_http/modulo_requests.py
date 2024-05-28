# O módulo requests permite enviar solicitações HTTP para servidores da web. Você pode criar solicitações
#  HTTP GET, POST, PUT, DELETE, PATCH e várias outras usando funções convenientes fornecidas pelo módulo.
#
# O requests também permite especificar parâmetros adicionais, como parâmetros de consulta,
# cabeçalhos personalizados e cookies, ao enviar solicitações HTTP.

# Após enviar uma solicitação HTTP, o requests recebe e retorna a resposta do servidor.
# Você pode acessar várias informações sobre a resposta, como o código de status, cabeçalhos e conteúdo da resposta.
import requests

# Iremos armazenas a URI para quem nossa requisição será destinada:
url = 'http://127.0.0.1:8080'
# Abaixo, iremos realizar nossa requisição, obtendo uma resposta em retorno:
response = requests.get(url)
# A partir dessa resposta, podemos obter informações como:
print('Resposta do servidor:', response)
print()
# O cabeçalho da resposta retornada pelo servidor:
print('Cabeçalho da resposta:', response.headers)
print()
# O corpo da resposta, contendo o conteúdo requisitado:
print('Corpo da resposta:', response.text)

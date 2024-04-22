import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8080/'
response = requests.get(url)
# Adquirindo o conteúdo HTML da página requisitada:
# raw_html = response.text
# Criando nosso objeto do tipo BeautifulSoup para trabalharmos com o HTML:
# parsed_html = BeautifulSoup(raw_html, 'html.parser')

# Obs.: Podemos ter problemas de codificação passando o HTML diretamente como instância
# de BeautifulSoup. Para resolvermos isso, podemos passar os bytes de nossa página HTML,
# especificando nossa codificação por parâmetro:
# Criando nosso objeto do tipo BeautifulSoup para trabalharmos com o HTML:

bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

# Exibindo o conteúdo do título da página:
if parsed_html.title is not None:
    print(parsed_html.title.text)
print()

# Com o método select_one, selecionamos apenas um elemento,
# e com select, selecionamos mais de um.
about_me = parsed_html.select_one('#first-section')

if about_me is not None:
    for p in about_me.select('p'):
        print(p.text)

from urllib.request import urlopen


def acessoSite(url):
    try:
        urlopen(url)
    except ():
        print('\n\033[31mO site está inacessível!\033[0m')
    else:
        print('\n\033[32mO site está acessível!\033[0m')


link = input('Informe o link do site que quer verificar o acesso: ')
acessoSite(link)

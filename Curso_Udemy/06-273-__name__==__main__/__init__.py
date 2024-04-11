# Como vimos anteriormente em nossas aulas de exportação e importação de módulos (04-153),
# quando executamos um módulo diretamente, percebemos que seu nome passar a ser __main__.
# Já quando executamos algum módulo importado, ele terá seu nome real. Dessa forma, para
# executarmos algum script somente se o executarmos diretamente, podmeos utilizar a condição:
if __name__ == '__main__':
    print('Estou sendo executado diretamente.')

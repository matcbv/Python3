import funcoes

lista_resp = ['desfazer', 'refazer', 'excluir', 'listar', 'limpar']

while True:
    print()
    print('Ações: refazer, desfazer, excluir, listar, limpar')
    resposta = input('Informe a ação a ser feita: ')
    if resposta not in lista_resp:
        funcoes.historico_respostas.append(resposta)
        funcoes.adicionar_dados(resposta)
    else:
        funcoes.chama_funcao(resposta)

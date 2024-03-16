# A recursão em Python, é o processo de dividir um problema em pequenas partes,
# para assim, ser solucionado.
# Na recursão, devemos ter um caso base para encerrar a recursão e um ou mais casos recursivos
# para resolverem as partes do nosso problema.
# Funções recursivas:
# Funções recursivas são funções que retornam a si mesmas.
# Quando uma função retorna a si mesma, ela é adicionada a pilha (stack) do Python. Todos as chamadas
# dessa função que são retornadas, vão sendo empilhados até que o caso base seja atendido.
# Quando a condição é atendida, o valor final é então retornado para a chamada anterior, e assim
# sucessivamente até que chegue à primeira chamada, para então ser exibido no console.
def somar(inicio=0, fim=5):
    print(inicio, fim)
    if inicio == fim:
        return inicio
    else:
        inicio += 1
        return somar(inicio, fim)


print(somar())
print('-'*10)


# Um exemplo que se encaixa muito bem no uso de funções recursivas é o cálculo fatorial. Ex.:
def fatorial(num):
    pass


print(fatorial(10))

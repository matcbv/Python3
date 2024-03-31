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
print('-' * 10)


# Um exemplo que se encaixa muito bem no uso de funções recursivas é o cálculo fatorial. Ex.:
def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num - 1)


# No exemplo acima, retornamos a função fatorial subtraindo 1 do valor de num.
# Quando num finalmente for 1, retornaremos 1 para o resultado da função anterior, que irá multiplicar
# o resultado, retornando esse para o resultado da anterior e assim sucessivamente. Ex.:
# fatorial(3) -> 3 * fatorial(2) -> 3 * 2 * fatorial(1) -> 3 * 2 * 1 -> 6

print(fatorial(5))

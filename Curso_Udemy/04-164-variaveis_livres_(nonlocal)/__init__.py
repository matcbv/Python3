# Variáveis livres são aquelas que não são definidas em um escopo local, mesmo estando
# presente neles. Em Python, não é possível modificar uma variável que não está presente
# no escopo local de sua função. Porém, ao definirmos ela como uma variável livre, isso
# passa a ser possível.

def caucular_somatorio():
    # A variável livre somatorio, terá seu valor atualizado cada vez que a função
    # for chamada.
    somatorio = 0

    def realizar_soma(numero_para_soma):
        # Com a palavra-chave nonlocal, definimos uma variável como livre,
        # permitindo-a ser modificada.
        nonlocal somatorio
        somatorio += numero_para_soma
        return somatorio

    return realizar_soma
# No exemplo acima, criamos um somatório que começa com o valo zero, e vai sendo implementado com mais valores a cada
# chamada da função. Poderíamos também definir um valor inicial para a variável somatória, recebendo-o por parâmetro na
# função caucular_somatorio e atribuindo-o à variável somatória. Ex.: def caucular_somatorio(num): {somatorio = num}


soma = caucular_somatorio()
soma(10)
soma(5)
resultado = soma(-4)
print(resultado)

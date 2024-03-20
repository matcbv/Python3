# É importante evitarmos o uso de condicionais em excesso, para deixarmos nosso código mais limpo e coeso.
# Uma das opções para isso é utilizamos o método de Guard Clause.
# Guard Clause é o nome do termo utilizado para a verificação de determinada condição, por uma declaração
# condicional no início de uma função. Essa, verifica se determinadas condições são atendidas e, se não
# forem, interrompe imediatamente a execução da função ou retorna um valor especial. Ex.:

def numero_ou_nao(valor):
    if isinstance(valor, int):
        return True
    return False


# Na função acima, temos uma verificação, que se atendida, irá retornar um determinado valor.
# Caso contrário, irá retornar logo em seguida o valor que não atende a condição.

# Também temos uma opção de utilizar o match case. No match case, passaremos um objeto, e os casos para
# cada valor possível informado. Ex.:

numero = 0

match numero:
    case 1:
        print('Número 1')
    case 2:
        print('Número 2')
    case 3:
        print('Número 3')
    case 4:
        print('Número 4')
    case _:
        print('Valor desconhecido.')

# Obs.: O valor _ possui o mesmo papel do else. Caso nenhum dos casos seja atendido, ele será realizado.

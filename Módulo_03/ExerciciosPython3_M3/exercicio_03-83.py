while True:
    frase = input('Informe uma frase qualquer, em que parênteses sejam utilizados: ')
    numD = numE = 0
    cond = ''
    if '(' not in frase and ')' not in frase:
        print('A frase informada acima não possui nenhum parênteses')
    else:
        numD = frase.count('(')
        numE = frase.count(')')
        if numD == numE:
            print('Os parênteses foram posicionados corretamente.')
        else:
            print('Os parênteses foram posicionados incorretamente.')
    cond = input('Deseja inserir uma nova frase para ser verificada? ')
    while cond not in 'SimsimNãoNaonãonao':
        cond = input('Resposta inválida. Informe uma nova resposta: ')
    if cond in 'NãoNaonãonao':
        break

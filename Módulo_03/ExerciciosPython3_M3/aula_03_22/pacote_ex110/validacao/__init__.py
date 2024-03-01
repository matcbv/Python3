def lerDinheiro():
    while True:
        val = input('\nInforme o valor do produto: ').replace(',', '.')
        result = 0
        try:
            result = float(val)
            valid = True
        except ValueError:
            valid = False
        if valid:
            return result
        else:
            print('Valor inválido!')

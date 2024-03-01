def multiplicar():
    def valores(num):
        return [num * 2, num * 3, num * 4]
    return valores


valor = multiplicar()
print(valor(int(input('Qual valor deseja multiplicar? '))))

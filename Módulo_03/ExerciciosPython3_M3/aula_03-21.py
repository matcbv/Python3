def somar(a=1, b=2):
    global num1, num2
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    print(a+b)


num1 = num2 = 0
somar(num1, num2)

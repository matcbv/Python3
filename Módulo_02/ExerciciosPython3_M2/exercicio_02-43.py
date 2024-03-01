peso = float(input('Informe o peso da pessoa, em Kg, a ser cauculado o IMC: '))
altura = float(input('Informe a altura da pessoa, em metros, a ser cauculado o IMC: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'A pessoa está abaixo do peso. Está com um IMC de {imc}')
elif imc < 25:
    print(f'A pessoa possui peso ideal! Está com um IMC de {imc}')
elif imc < 30:
    print(f'A pessoa possui sobrepeso. Está com um IMC de {imc}')
elif imc < 40:
    print(f'A pessoa possui obesidade. Está com um IMC de {imc}')
else:
    print(f'A pessoa possui obesidade mórbida. Está com um IMC de {imc}')

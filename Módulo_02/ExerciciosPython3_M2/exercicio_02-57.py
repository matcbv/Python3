
sexo = input('Informe a seguir, o sexo do indivíduo: ').upper()
while sexo != 'M' and sexo != 'F': # Podemos também utilizar a condiçao while sexo not in 'MF':
    print('Sexo não reconhecido. Tente novamente\n')
    sexo = input('Informe a seguir, o sexo do indivíduo: ').upper()
print('Confirmado!')

reta1 = int(input('Informe a primeira reta: '))
reta2 = int(input('Informe a segunda reta: '))
reta3 = int(input('Informe a terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Tais retas podem formar um triângulo.')
    if reta1 == reta2 == reta3:
        print('O triângulo formado é equilátero.')
    elif reta1 != reta2 != reta3 != reta1:
        print('O triângulo formado é isósceles.')
    else:
        print('O triângulo formado é escaleno.')
else:
    print('Tais retas não podem formar um triângulo.')

reta1 = int(input('Digite a seguir, o tamanho da primeira reta: '))
reta2 = int(input('Digite a seguir, o tamanho da segunda reta: '))
reta3 = int(input('Digite a seguir, o tamanho da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas informadas acima podem formar um triângulo!')
else:
    print('As retas informadas acima não podem formar um triângulo!')

frase = input('Informa a seguir, a frase a ser verificada: ').upper().split()
frase = ''.join(frase)
'''quant = len(frase)
cont = 0
c = 0'''
inverso: ''
inverso = frase[::-1]

print(inverso)
if inverso == frase:
    print('A frase informada acima é um políndromo.')
else:
    print('A frase informada acima não é um políndromo.')

# Segunda opção de resolução:

'''for i in range(quant - 1, -1, -1):
  if frase[i] == frase[c]:
    cont += 1 
  c += 1'''

'''if cont == quant:
  print('A frase informada acima é um políndromo.')
else:
  print('A frase informada acima não é um políndromo.')'''

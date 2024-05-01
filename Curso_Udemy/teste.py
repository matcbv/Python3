class OpenFileError(Exception):
    ...


num1 = 10
num2 = 0

try:
    num1 / num2
except OpenFileError as e:
    print('Não foi possível realizar o envio do email. Tente novamente.', e)
else:
    print('Email enviado com sucesso!')

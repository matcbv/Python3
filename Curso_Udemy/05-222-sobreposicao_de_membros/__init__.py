# Ao lidarmos com herança, a chamada sobreposição de membros pode acabar ocorrendo. Isso ocorre quando temos
# dois métodos ou atributos de mesmo nome em diferentes classes.

# Aqui estaremos herdando os métodos contidos na classe str:
class MinhaString(str):
    # Estaremos definindo um método chamado upper em nossa classe MinhaString, porém isso estará afetando o
    # funcionamento do atributo upper da classe str. Para podermos utilizar o método da classe str,
    # estaremos utilizando a classe super. Através dela, estaremos chamando determinado método de nossa superclasse.
    def upper(self):
        print('Método upper foi chamado.')
        # Com a função super, estaremos chamando a função upper da superclasse. A função super
        # aceita dois parâmetros, sendo o primeiro, classe que irá servir de início para a
        # requisição do método, e o segundo será a instância atual da classe. Os valores
        # padrão são super(Casse_Atual, self).
        # Obs.: A classe atual é ignorada. A busca é feita a partir da classe especificada.
        resultado = super().upper()
        print('Conversão realizada com sucesso!')
        return resultado


# Criando um objeto para receber uma string através da classe MinhaString.
texto = MinhaString('Um texto qualquer')
# Chamando o método upper:
maiusculo = texto.upper()
print(maiusculo)
print('-' * 30)


# Podemos ainda ter casos de herança múltipla, que veremos posteriormente. Vamos ver um exemplo
# simples para ilustrarmos nosso exemplo:

# A instância obj, terá todas as variáveis das superclasses superiores, porém o método
# da classe C será prevalecido dos demais. Para termos acesso aos métodos das classes B e A,
# utilizaremos a função super.
class A:
    objeto_a = 'A'

    def mensagem(self):
        print('Classe A')


class B(A):
    objeto_b = 'B'

    def mensagem(self):
        print('Classe B')


class C(B):
    objeto_c = 'C'

    def mensagem(self):
        print('Classe C')
        super(C, self).mensagem()
        super(B, self).mensagem()


obj = C()
print(obj.objeto_a, obj.objeto_b, obj.objeto_c)
obj.mensagem()

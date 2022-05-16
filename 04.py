#Exercicio 4
'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

    a. Atributos: nome, idade, peso e altura
    b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.anos = anos
        self.idade += anos
        print('\nA pessoa envelheceu ',anos,' anos\nA idade atual é ',self.idade,' anos')

    def engordar(self, pesagem):
        self.peso += pesagem
        print('\nA pessoa engordou ',pesagem,' kg\nO peso atual é',round(self.peso),'kg')

    def emagrecer(self, pesagem):
        self.peso -= pesagem
        print('\nA pessoa emagreceu ',pesagem,' kg\nO peso atual é',round(self.peso),'kg')

    def crescer(self, anos):
        self.idade += anos
        if self.idade < 21:
            crescimento = 0.05 * anos
            self.altura += crescimento
            print('\nA pessoa cresceu ',crescimento,'m\nA altura atual é',self.altura,'m')
        else:
            print('\nA pessoa não cresceu')

#Teste Classe
pessoa_1 = Pessoa('João', 10, 80.60, 1.90)

print(pessoa_1.nome)
pessoa_1.envelhecer(5)
pessoa_1.engordar(10.1)
pessoa_1.emagrecer(5)
pessoa_1.crescer(4)
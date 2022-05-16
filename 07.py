#Exercicio 7
'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

    a. Atributos: Nome, Fome, Saúde e Idade 
    b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
    Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''

class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.Nome = Nome
        self.Fome = Fome
        self.Saude = Saude
        self.Idade = Idade

    def alt_Nome(self, Nome):
        self.Nome = Nome

    def alt_Fome(self, Fome):
        self.Fome = Fome

    def alt_Saude(self, Saude):
        self.Saude = Saude
        
    def alt_Idade(self, Idade):
        self.Idade = Idade

    def CheckHumor(self): 
        if self.Fome > 7 or self.Saude <= 3:
            return 'está mal-humorado'
        else:
            return 'está de bom humor'
    #tambem é possivel inserir um valor de pontuação no nivel do humor como no enunciado
            
    def DarComida(self):
        if self.Fome <= 10 and self.Fome > 0:
            self.Fome -= 1
            
#Teste Classe
dino = Tamagushi('Tobias')
dino.alt_Nome('Jojo')
dino.alt_Fome(9)
dino.alt_Saude(5)
dino.alt_Idade(10)
dino.DarComida()
dino.DarComida()
dino.DarComida()

print('Nome:',dino.Nome)
print(dino.Fome,'de fome')
print(dino.Saude,'de saúde')
print(dino.Idade,'anos')
print('O bichinho',dino.CheckHumor())
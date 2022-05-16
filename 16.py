#Exercicio 16
'''
Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.
'''
class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.alt_Nome(Nome)
        self.alt_Fome(Fome)
        self.alt_Saude(Saude)
        self.alt_Idade(Idade)

    def alt_Nome(self, Nome):
        self.Nome = Nome

    def get_Nome(self):
        return self.Nome

    def alt_Fome(self, Fome):
        self.Fome = Fome

    def get_Fome(self):
        return self.Fome

    def alt_Saude(self, Saude):
        self.Saude = Saude

    def get_Saude(self):
        return self.Saude
        
    def alt_Idade(self, Idade):
        self.Idade = Idade

    def get_Idade(self):
        return self.Idade

    def CheckHumor(self): 
        if self.Fome > 7 or self.Saude <= 3:
            return 'está mal-humorado'
        else:
            return 'está de bom humor'
    #tambem é possivel inserir um valor de pontuação no nivel do humor como no enunciado

    def get_Humor(self):
        return self.get_Fome() * self.get_Saude()
            
    def DarComida(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Fome -= self.Fome * (Quantidade / 100.0)

    def brincar(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Saude += self.Saude * (Quantidade / 100.0)

    def str(self):
        print('\n--STATUS--')
        print('Nome:', self.get_Nome())
        print('Idade:', self.get_Idade())
        print('Fome:', self.get_Fome())
        print('Saude:', self.get_Saude())
        print('Humor:', self.get_Humor())
            
#Teste Classe
dino = Tamagushi('Tobias')
dino.alt_Nome('Jojo')
dino.alt_Fome(9)
dino.alt_Saude(5)
dino.alt_Idade(10)
dino.DarComida(50)
dino.brincar(8)

print('Nome:',dino.Nome)
print(dino.Fome,'de fome')
print(dino.Saude,'de saúde')
print(dino.Idade,'anos')
print('O bichinho',dino.CheckHumor())
dino.str()
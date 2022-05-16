#Exercicio 2
'''
Classe Quadrado: Crie uma classe que modele um quadrado:

    a. Atributos: Tamanho do lado
    b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

'''

class Quadrado:
    def __init__(self, Tamanho_do_lado):
        self.Tamanho_do_lado = Tamanho_do_lado

    def Mudar_valor_do_Lado(self, Tamanho_do_lado):
        self.Tamanho_do_lado = Tamanho_do_lado

    def Retornar_Valor_do_Lado(self):
        return self.Tamanho_do_lado

    def Calcular_Area(self):
        return self.Tamanho_do_lado * self.Tamanho_do_lado

#Teste Classe
quadrado_1 = Quadrado(2)
quadrado_1.Mudar_Valor_do_Lado(6)
print('O valor do Lado do Quadrado é: ', quadrado_1.Retornar_Valor_do_Lado())
print('O valor da Área do Quadrado é: ', quadrado_1.Calcular_Area())
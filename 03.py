#Exercicio 3
'''
Classe Retangulo: Crie uma classe que modele um retangulo:

    a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo:
    def __init__(self, Comprimento, Largura):
        self.Comprimento = Comprimento
        self.Largura = Largura

    def Mudar_valor_dos_Lados(self, Comprimento, Largura):
        self.Comprimento = Comprimento
        self.Largura = Largura

    def Retornar_valor_dos_Lados(self):
        return self.Comprimento, self.Largura

    def Calcular_Area(self):
        return self.Comprimento * self.Largura

    def Calcular_Perimetro(self):
        return (2 * self.Comprimento) + (2 * self.Largura)

LadoA = int(input('digite o comprimento: '))
LadoB = int(input('digite a largura: '))

#Teste Classe
retangulo_1 = Retangulo(LadoA,LadoB)

print('\nO valor da Área do Retangulo é: ',retangulo_1.Calcular_Area())
print('\nO valor do Perímetro do Retangulo é: ',retangulo_1.Calcular_Perimetro())

print('\nSerão necessarios ',retangulo_1.Calcular_Area(),' pisos e ',retangulo_1.Calcular_Perimetro(),' rodapés')
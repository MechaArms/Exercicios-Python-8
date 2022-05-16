#Exercicio 8
'''
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
'''

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida): 
        self.bucho.append(comida)

    def verBucho(self):
        print(f'O bucho do Macaco {self.nome} possui dentro dele:\n {self.bucho}')

    def digerir(self):
        comida_permitida = ['banana','pera','manga']
        for i in range(len(self.bucho)):
            if self.bucho[i] in comida_permitida:
                print(f'O item {self.bucho[i]} foi digerido no bucho do Macaco {self.nome}')
            else:
                print(f'O item {self.bucho[i]} não foi digerido no bucho do Macaco {self.nome}, ele o vomitou')

#Teste Classe
Macaco1 = Macaco('Xita') 
Macaco2 = Macaco('Mamaco') 

Macaco1.comer('abacaxi')
Macaco1.comer('limão')
Macaco1.comer('pera')
Macaco1.verBucho()
Macaco1.digerir()
print('\n')
Macaco2.comer('banana')
Macaco2.comer('laranja')
Macaco2.comer('manga')
Macaco2.comer(Macaco1) #Teste de macaco canibal, por ser objeto o nome do item aparece bugado, mas ele segue o programa avisando que não é possivel digeri-lo, se usar como 'Macaco.nome' o nome sai correto no programa
Macaco2.verBucho()
Macaco2.digerir()
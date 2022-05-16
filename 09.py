#Exercicio 9
'''
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

    a.Possua uma classe chamada Retangulo, com os atributos largura e altura.
    b.Possua uma classe chamada Ponto, com os atributos x e y.
    c.Possua uma função para imprimir os valores da classe Ponto
    d.Possua uma função para encontrar o centro de um Retângulo.
    e.Você deve criar alguns objetos da classe Retangulo.
    f.Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
    g.A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
    h.O valor do centro do objeto deve ser mostrado na tela
    i.Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
'''

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self): 
        if self.largura %2 == 1 and self.altura %2 == 1:
            larguraCentro = (self.largura /2) + 0.5
            alturaCentro = (self.altura /2) + 0.5
            print(f'\nO centro do retangulo está na posição:\nLargura: {larguraCentro:.0f}\nAltura: {alturaCentro:.0f}')
        else:
            print(f'\Impossivel achar o centro pois os valores não são impares')
    
class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimirPonto(self):
        if self.x == 0 or self.y == 0:
            p = Ponto.pontoPartida(self)
            print(f'\nO ponto está na posição inicial:\nLargura: {p[0]}\nAltura: {p[1]}')
        else:
            print(f'\nO ponto está na posição:\nLargura: {self.x}\nAltura: {self.y}')
  
    def pontoPartida(self):
        larguraInicial = 2
        alturaInicial = self.y - 1
        print(f'\nO ponto está na posição inicial:\nLargura: {larguraInicial}\nAltura: {alturaInicial}')
        inicioPonto = [larguraInicial, alturaInicial]
        return inicioPonto  

#Teste Classe
quad1 = Retangulo(7,5)
quad1.encontrarCentro()

quad1 = Ponto(5,6)
quad1.imprimirPonto()
quad1.pontoPartida()
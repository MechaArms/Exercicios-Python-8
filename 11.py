#Exercicio 11
'''
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

    Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
    a. O consumo é especificado no construtor e o nível de combustível inicial é 0.
    b. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
    c. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    d. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

    meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
    meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
    meuFusca.andar(100);            # anda 100 quilômetros.
    meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
'''

class Carro:

    def __init__(self, quilometrosLitro):
        self.quilometrosLitro = quilometrosLitro
        self.qtdeCombustivel = 0

    def adicionarGasolina(self, quantidade):
        self.qtdeCombustivel += float(quantidade)

    def andar(self, distancia):
        gasto = distancia / self.quilometrosLitro
        self.qtdeCombustivel -= gasto

    def obterGasolina(self):
        print(f'{self.qtdeCombustivel:.2f}')

#Teste Classe
meuFusca = Carro(15)
# 15 quilometros por litro de combustivel.
meuFusca.adicionarGasolina(20)
# abastece com 20 litros de combustivel.
meuFusca.andar(100)
# anda 100 quilometros.
meuFusca.obterGasolina()
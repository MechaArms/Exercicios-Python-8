#Exercicio 10

'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

a.Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
      I.tipoCombustivel.
     II.valorLitro
    III.quantidadeCombustivel
b.Possua no mínimo esses métodos:
      I.abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
     II.abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    III.alterarValor( ) – altera o valor do litro do combustível.
     IV.alterarCombustivel( ) – altera o tipo do combustível.
      V.alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''

class BombaCombustivel():

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLitro)
        self.setQuantidadeCombustivel(quantidadeCombustivel)

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)

    def abastecerPorLitro(self, totalLitros):
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)

# Teste da classe
bomba1 = BombaCombustivel('Gasolina', 7.50, 1000)
bomba1.abastecerPorLitro(100)
print(f'A quantidade na bomba é: {bomba1.quantidadeCombustivel:.2f} litros')
bomba1.abastecerPorValor(100)
print(f'A quantidade na bomba é: {bomba1.quantidadeCombustivel:.2f} litros')
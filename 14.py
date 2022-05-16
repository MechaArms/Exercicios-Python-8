#Exercicio 14
'''
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
   harry=funcionário("Harry",25000)
   harry.aumentarSalario(10)

'''
class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100.0)
        
#Teste Classe
harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)
print (f'Nome: {harry.getNome()}')
print (f'Salario: R$ {harry.getSalario():.2f}')
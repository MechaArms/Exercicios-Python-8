#Exercicio 13
'''
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). 
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. 
Escreva um pequeno programa que teste sua classe.
'''

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

#Teste Classe
func1 = Funcionario('Morales Moreno', 1150.90)
print (f'Nome: {func1.getNome()}')
print (f'Salario: R$ {func1.getSalario():.2f}')
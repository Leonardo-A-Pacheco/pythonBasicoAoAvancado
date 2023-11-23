# classes são moldes para criar novos objetos
# as classes geram objetos (instancias) que 
# podem ter seus proprios metodos.
# os objetos gerados pela classe podem usar seus dados internos
# para realizar ações
# por convenção usamos PascalCase para nomes de classes

# string = 'leonardo'
# print(string.upper())
# print(isinstance(string, str))

# class CriarBaseDeDados:

class Pessoa:
    #init  é utilazado para inicializar os atributos dentro da classe
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

# p1 é a instancia da classe que é o self
p1 = Pessoa('leo','Pacheco')
# p1.nome ='leo'
# p1.sobrenome ='pacheco'

p2 = Pessoa('Mulher','gato')
# p2.nome ='Alpha'
# p2.sobrenome ='Bravo'

print(p1.nome)
print(p1.sobrenome)
print('\n')

print(p2.nome)
print(p2.sobrenome)
print('\n')













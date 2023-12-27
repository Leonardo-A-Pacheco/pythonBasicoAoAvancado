# Herança simples - Relações entre classes
# Associação - usa, 
# Agregação - tem
# Composição - É dono de, 
# Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class Qualquer:
#     ...
# help(Qualquer)

# class Qualquer(object):
#     ...
# help(Qualquer)

class Pessoa:
    cpf = 1234

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('classe pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    print('não saí da classe pessoa')
    ...

class Aluno(Pessoa):
    cpf = 4331
    ...


c1 = Cliente('leonardo', 'com calor')
c1.falar_nome_classe()
print(c1.nome, c1.sobrenome)
# help(Cliente)
print(c1.cpf)
print()

a1 = Aluno('pacheco', 'com fome')
a1.falar_nome_classe()
print(a1.nome, a1.sobrenome)
print(a1.cpf)
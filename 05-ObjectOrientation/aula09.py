# metodos de classe + factories
# são metodo onde "self" sera cls ou seja
# ao inves de receber a instancia no primeiro parametro receberemos a propria classe

class Pessoa:
    ano = 2023 #atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey')
   
    @classmethod
    def criar_50_anos(cls, nome):
        return cls(nome, 50)
   
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('anonima', idade)


print(Pessoa.ano)

p1 = Pessoa('joão',34)
Pessoa.metodo_de_classe()
print(p1.nome, p1.idade)
print()
p2 = Pessoa.criar_50_anos('helena')
Pessoa.metodo_de_classe()
print(p2.nome, p2.idade)

print()
p3 = Pessoa.criar_sem_nome(11)
print(p3.nome, p3.idade)
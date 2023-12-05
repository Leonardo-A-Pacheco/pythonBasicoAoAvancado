# __dict__ e vars para atributos de instancia
class People:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

p1 = People('polaco', 3)

print(p1.idade)
# del p1.nome
print(p1.nome)
print(p1.get_ano_nascimento())
print()
print(p1.__dict__)
print(vars(p1))

p1.__dict__['moliana'] = 52
print()
print(vars(p1))
print()

dados = vars(p1)

print(f'{dados}')



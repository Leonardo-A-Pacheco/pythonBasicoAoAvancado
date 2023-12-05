#atributos de classe

class People:
    ano_atual = 2023

    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return People.ano_atual - self.idade
    
p1 = People('Odracir', 25)
p2 = People('Odranoel', 31)

print(People.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())



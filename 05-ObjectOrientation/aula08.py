# salve sua classe em json 
# salve os dados da sua classe em json
# crie novamente instancias 
# de classe com os dados salvos
# faça em arquivos separados

import json

CAMINHO_ARQUIVO = 'aula08.json'

class Pessoa:
    def __init__(self, nome, idade): 
        self.nome = nome
        self.idade = idade

p1 = Pessoa('joão', 33)
p2 = Pessoa('joaquina', 3)
p3 = Pessoa('belarmino', 13)

bd = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('fazendo dump')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
        #criado arquivo aula08.json

print(__name__)

































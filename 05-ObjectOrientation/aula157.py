# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum
       
# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA', 'ACIMA', 'ABAIXO'])

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

class Mover:
    def __init__(self, mover='objeto'):
        self.nome = mover
        
    def mover(self, direcao: Direcoes):
    
        if not isinstance (direcao, Direcoes):
        # if direcao not in ['esquerda', 'direita','acima','abaixo']:
            raise ValueError('direcao nao encontrada')
        # print(f'Movendo para {direcao}')
        print(f'Movendo para {direcao.name} ({direcao.value})')
m = Mover('coisa')

m.mover(Direcoes.ESQUERDA)
m.mover(Direcoes.DIREITA)
m.mover(Direcoes.ACIMA)
m.mover(Direcoes.ABAIXO)
# m.mover('diagonal')
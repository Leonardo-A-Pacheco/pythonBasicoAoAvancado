#formas de chamada da classe

class Carro:
    
    def __init__(self,nome='sem nome' ):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...\n')

fusca = Carro('fusca')
fusca.acelerar()

# ou
#
Carro('celta').acelerar()

# ou

caminhonete = Carro('pampa')
Carro.acelerar(caminhonete)

# ou

Carro().acelerar()
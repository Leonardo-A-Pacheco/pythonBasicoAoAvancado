# setter()
# variaveis com um anderline na frente ou dois anderlines
# são exclusivos e protegidos da classe e nao devem ser usados

class Caneta:
    def __init__(self, cor):
        # private prptected
        # self.cor_tinta = cor
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('property')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print(f'Estou no setter {valor}')
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('azul')
caneta.cor = 'rosa'
caneta._cor_tampa = 'pink'

print(caneta.cor)
print(caneta.cor_tampa)

# @property - é um getter no modo pythonico getter um metodo para obter um atributo modo pythonico - modo do python de fazer as coisas @property é uma propriedade do objeoto, ela é um metodo que se comporta como um Attributo 
# geralmente é usada nas seguintes situações:
# - como getter
# - evitar quebra de codigo do cliente
# - habilitar setter
# - executar ações ao obter atributos
# codigo cliete é o codigo que usa seu codigo

class Caneta:
    def __init__(self, cor):
        # private prptected public
        self.cor_tinta = cor
    
    # def get_cor(self):
    #     return self.cor
  
    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return self.cor_tinta
    



caneta = Caneta('Azul')
# print(caneta.get_cor())
print(caneta.cor)
print(caneta.cor_tampa)











class Animal:
    def __init__(self, tipo):
        self.tipo = tipo
        print(f' Animal {self.tipo} criado')

    def imprimir(self):
        print(f'Este é um animal {self.tipo}')

    def comer(self):
        print(f'{self.tipo} comendo')

    def emitir_som(self):
        print(self.tipo)
        

class Cachorro(Animal):
    
    def __init__(self):
        super().__init__('Cachorro')
        # print('objeto cachorro criado')

    def emitir_som(self):
        return('au-au')

class Gato(Animal):
    
    def __init__(self):
        super().__init__('Gato')
        # print('objeto gato criado')

    def emitir_som(self):
        return('miau')
    
dog = Cachorro()
dog.imprimir()
print(dog.emitir_som())
dog.comer()

print()

cat = Gato()
cat.imprimir()
print(cat.emitir_som())
cat.comer()

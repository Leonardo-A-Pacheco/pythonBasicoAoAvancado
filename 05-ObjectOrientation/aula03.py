# metodos em instancias de classes
# hard coded é um atributo fixo ja na classe

class carro:
    def __init__(self, nome='não declarou'):
        # self.nome = 'del_rey' #hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...\n')
   
    def frear(self):
        print(f'{self.nome} está freando...\n')
    
    def abastecer(self):
        print(f'{self.nome} está abastecendo...\n')


del_rey = carro('Do Rei')
print(del_rey.nome)
del_rey.acelerar()

mustang = carro('Ford Cobra')
print(mustang.nome)
mustang.abastecer()

uno = carro()
print(uno.nome)
uno.frear()

# exemplo de aplicação de metodo na instancia string
string = 'parametro minusculo'
print(string.upper())



















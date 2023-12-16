# exercicio com classes
# crie a classe carro none
# crie a classe motor none
# crie a classe fabricante none
# faça a ligação entre carro e motor 
# obs um motor pode ser de varios carros
# faça a ligação entre o carro e 
# fabricante
# obs um fabricante pode fabricar varios carros
# exiba o nome do carro motor e fabricante na tela


class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor= None
        self._fabricante = None
        
    
    @property
    def motor(self):
        return self._motor
   
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    
    @property
    def motor(self):
        return self._motor
   
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self.fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class fabricante:
    def __init__(self, nome):
        self.nome = nome

fuque = Carro('fuscao')
fuque.motor = 'v8'
fuque.fabricante = 'banana'

print(fuque)
 
 
# cria-se uma instancia para cada classe interna,

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)




b
pi = 3.1416

class Circulo:
    
    def __init__(self, raio = 5):
        self.raio = raio

    def area(self):
        return (self.raio * self.raio) * pi
    
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    def getRaio(self):
        return self.raio
    
c = Circulo()

print(c.getRaio())

print(c.area())

c.setRaio(7)

print(c.area())
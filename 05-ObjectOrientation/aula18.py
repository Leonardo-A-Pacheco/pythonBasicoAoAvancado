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

# class Carros:
#     def __init__(self, nome, marca) -> None:
#         self.nome = nome=[]
#         self.marca = marca=[]
    
# class Motor:
#     def __init__(self, modelo, carro) -> None:
#         ...

# class Fabricante:
#     def __init__(self, marca) -> None:
#         ...
# class Motor:
#     def __init__(self, modelo):
#         self.modelo = modelo
#         self.carros = []

#     def adicionar_carro(self, carro):
#         self.carros.append(carro)

# class Fabricante:
#     def __init__(self, marca):
#         self.marca = marca
#         self.carros_fabricados = []

#     def fabricar_carro(self, carro):
#         self.carros_fabricados.append(carro)

# class Carro:
#     def __init__(self, nome, fabricante):
#         self.nome = nome
#         self.fabricante = fabricante
#         self.motor = None

#     def adicionar_motor(self, motor):
#         self.motor = motor
#         motor.adicionar_carro(self)

#     def exibir_informacoes(self):
#         print(f"Carro: {self.nome}")
#         print(f"Fabricante: {self.fabricante.marca}")
#         print(f"Motor: {self.motor.modelo}")

# # Exemplo de uso:

# # Criando instâncias
# motor1 = Motor(modelo="Motor A")
# motor2 = Motor(modelo="Motor B")

# fabricante1 = Fabricante(marca="Fabricante X")
# fabricante2 = Fabricante(marca="Fabricante Y")

# carro1 = Carro(nome="Carro1", fabricante=fabricante1)
# carro2 = Carro(nome="Carro2", fabricante=fabricante2)

# # Estabelecendo relações
# carro1.adicionar_motor(motor1)
# carro2.adicionar_motor(motor2)

# fabricante1.fabricar_carro(carro1)
# fabricante2.fabricar_carro(carro2)

# # Exibindo informações
# carro1.exibir_informacoes()
# carro2.exibir_informacoes()

class Carro:
    def __init__(self, nome, fabricante):
        self.nome = nome
        self.fabricante = fabricante
        self.motor = None

    def adicionar_motor(self, motor):
        self.motor = motor
        motor.adicionar_carro(self)

    def exibir_informacoes(self):
        print(f"Carro: {self.nome}")
        print(f"Fabricante: {self.fabricante.marca}")
        print(f"Motor: {self.motor.modelo}")


class Motor:
    def __init__(self, modelo):
        self.modelo = modelo
        self.carros = []

    def adicionar_carro(self, carro):
        self.carros.append(carro)


class Fabricante:
    def __init__(self, marca):
        self.marca = marca
        self.carros_fabricados = []

    def fabricar_carro(self, carro):
        self.carros_fabricados.append(carro)


# Exemplo de uso:

# Criando instâncias
fabricante1 = Fabricante(marca="Fabricante X")
fabricante2 = Fabricante(marca="Fabricante Y")

carro1 = Carro(nome="Carro1", fabricante=fabricante1)
carro2 = Carro(nome="Carro2", fabricante=fabricante2)

motor1 = Motor(modelo="Motor A")
motor2 = Motor(modelo="Motor B")

# Estabelecendo relações
carro1.adicionar_motor(motor1)
carro2.adicionar_motor(motor2)

fabricante1.fabricar_carro(carro1)
fabricante2.fabricar_carro(carro2)

# Exibindo informações
carro1.exibir_informacoes()
carro2.exibir_informacoes()

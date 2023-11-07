# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

c = ['Salvador', 'Ubatuba', 'Belo Horizonte']
e = ['BA', 'SP', 'MG', 'RJ']

def menor(*args):
    return (min(len(lista) for lista in args))

print(menor(c, e))
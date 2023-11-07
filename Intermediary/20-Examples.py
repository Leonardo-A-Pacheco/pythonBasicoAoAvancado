# print('condicionais')

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numeros)

# novo_numeros = [numero for numero in numeros if numero > 5]
# print(novo_numeros)

# impares = [numero for numero in numeros if numero % 2 != 0]
# print(impares)

# pares = [numero for numero in numeros if numero % 2 == 0]
# print(pares)

# outro_if = [
#     numero
#     if numero != 6 else 600
#     for numero in pares
# ]
# print(outro_if)
# print('---------------------------------------')

# numeros = [[numero, numero ** 2] for numero in range(10)]
# print(f'numeros \n {numeros}\n')

# flat = [y for x in numeros for y in x]
# print('flat')
# print(flat)
# print('---------------------------------------')
# print('linhas_e_colunas\n')

# linhas_e_colunas = [
#     (x, y)
#     if y != 2 else (x, y * 1000)
#     for x in range(1, 11)
#     for y in range(1, 6)
#     if x != 2
# ]
# print('---------------------------------------\n')
# print('novos_nomes')

# print(linhas_e_colunas)

# nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
# novos_nomes = [
#     f'{nome[:-1].lower()}{nome[-1].upper()}'
#     for nome in nomes
# ]
# print(novos_nomes)

# print('---------------------------------------\n')

print('\nutilização')

def divisãoFn(x, y):
    return x / y


def multiplicaçãoFn(x, y):
    return x * y


def potenciaçãoFn(x, y):
    return x ** y


numeros = [n for n in range(6)]
divisão = [divisãoFn(numero, 2) for numero in numeros]
multiplicação = [multiplicaçãoFn(numero, 2) for numero in numeros]
quadrado = [potenciaçãoFn(numero, 2) for numero in numeros]

print(numeros)
print(divisão)
print(multiplicação)
print(quadrado)


















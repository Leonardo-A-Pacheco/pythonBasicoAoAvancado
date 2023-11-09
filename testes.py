

a = ['banana']
b = ['i']
a += join(b)

print(a)

# def menor(*args):
#     print(min(len(lista) for lista in args))

# c = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# e = ['BA', 'SP', 'MG', 'RJ']

# menor(c, e)  # Passa as listas c e e como argumentos






# numeros = [2, 3, 4, 5, 6, 7, 8, 5, 4, 3, 4, 6, 43]

# numerosDuplicados = [2 * n if n < 5 else 7 * n for n in numeros]

# print(numeros)
# print(numerosDuplicados)


# ldl = [
#     [10, 2, 3, 4, 5, 6, 7, 3, 2, 10],
    
#     [1, 2, 3, 4, 5, 5, 7, 8, 9, 10],
    
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]

# dup = 0

# for i in range(len(ldl)):
#     print
#     t = len(ldl[i])
#     for e in range(t // 2):

#         esquerda = ldl[i][e]   
#         direita = ldl[i][-1 -e]
#         # print(f"{esquerda} com {direita}")
#         if (esquerda == direita):
#             dup += 1
#         if (esquerda == direita) and e >= 1 and dup == 2:
#             print(f'primeiro duplicado da lista {e}:  {esquerda}')
string = 'ABCD'

lista = ['Moly','Polaco', 1, 2, 3, 4, 'Rayca', 'Brown']


# print(f'{string}\n')


# for letra in string:
#     print(f'{letra}')

# print('')

# for letra in string:
#     print(f'{letra}', end="")

# print('\n')

# #desenpacotamento
# m, p, n1, n2, n3, n4, r, b = lista

# print(m, p, n1, n2, n3, n4, r, b)

# #desempacotamento selecionado
# m, p, n1, n2, *_, = lista 

# print(m, p, n1, n2)

#os primeiros depois do ignorador os ultimos
#1º2º ... 7º8º 
m, p, *_, r, b = lista

print(m, p, r, b) 

#isto 
print(*lista)




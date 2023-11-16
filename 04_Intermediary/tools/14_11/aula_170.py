# exercicio - unir listas
# crie uma função ziper como um ziper de roupas
# o trabalho dessa funçao sera unir duas listas na ordem
# use todos os valores da menor lista 
# ['salvador', 'ubatuba', 'belo horizinte',]
# ['ba', 'sp', 'mg', 'rj']

# resultado

# [('salvador', 'ba'), ('ubatuba', 'sp'), ('belo horizonte', 'mg')]

def menor_lista(lista1, lista2):
    if   len(lista1) < len(lista2):
        menor = lista1
    #     print(menor)
    else:
        menor = lista2
    #     print(menor)
    return menor
    

l1 = ['salvador', 'ubatuba', 'belo horizinte',]
l2 = ['ba', 'sp', 'mg', 'rj']

# Lista_menor = menor_lista(l1, l2)

def ziper(lista1, lista2):
    intervalo_max = min(len(lista1), len(lista2))
    #retornando uma list comprehension do menor tamanho com tuplas concatenadas
    return [
      (lista1[i], lista2[i]) for i in range(intervalo_max)
    ]

# print(ziper(l1, l2))

print(list(zip(l1,l2)))
#zip retorna um iterator
print()

for i in zip(l1, l2):
    print(i)

print()
#ou ainda importar um modulo
from itertools import zip_longest

print(list(zip_longest(l1, l2, fillvalue='sem cidade')))



 
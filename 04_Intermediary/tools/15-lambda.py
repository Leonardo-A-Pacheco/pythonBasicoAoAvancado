# lambda são funções anonimas que contem apenas uma linha de uma unica expressão

import copy

lista_dic = [
    {'nome': 'alberto', 'sobrenome': 'zanin'},
    {'nome': 'bruno', 'sobrenome': 'wolk'},
    {'nome': 'Carolina', 'sobrenome': 'York'},
    {'nome': 'Duda', 'sobrenome': 'Xaxim'},
    {'nome': 'Etephany', 'sobrenome': 'Vargas'},
    {'nome': 'Fernando', 'sobrenome': 'Urach'},
]

# lista = [1, 6, 2, 5, 8, 3, 5, 78, 5, 3, 5]
# print(lista)
# lista_sort = sorted(lista)
# print(lista_sort)

# dicionarios não são ordenados automaticamente pelo python

def order_name(item):
    return item['nome']

def order_lastname(item):
    return item['sobrenome']

def exibir(lista):
    for i in lista:
        print(i)
        

# usando sort para apenas exiber organizado

# lista_dic.sort(key=order_name)

# for i in lista_dic:
#     print(i)

# print()

# lista_dic.sort(key=order_lastname)

# for i in lista_dic:
#     print(i)

# usando lambda functions

# lista_dic.sort(key=lambda item: item['nome'])

# for i in lista_dic:
#     print(i)

# print()
# lista_dic.sort(key=lambda item: item['sobrenome'])

# for i in lista_dic:
#     print(i)

#lembrando que sort só ordena para exibição e o sorted altera a lista e tambem pode ser atribuido dentro de outras variaveis ex:

var_sorted_name = sorted(lista_dic, key=lambda item: item['nome'])

exibir(var_sorted_name)

print()
var_sorted_lastname = sorted(lista_dic, key=lambda item: item['sobrenome'])

# exibir é equivalente a esse loop abaixo
for i in var_sorted_lastname:
    print(i)

 
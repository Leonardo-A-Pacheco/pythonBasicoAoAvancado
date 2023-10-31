# list comprehension é uma forma rapida para criar listas a partir de iteraveis

# print(list(range(10)))

lista = []

for i in range(10):
    lista.append(i)
# print(lista)

list_comprehension = [n*2 for n in range(10)]

# print(list_comprehension)  

produtos =[
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
    {'nome': 'p4', 'preco': 50},
]
 
#mapeamento de uma list comprehension de produto
# print()
# novos_produtos = [
#     produto for produto in produtos        
# ]

# print(*novos_produtos, sep='\n')

# print()
# novos_produtos = [
#     produto['nome'] for produto in produtos        
# ]

# print(*novos_produtos, sep='\n')


# print()
# novos_produtos = [
#     {'nome':produto['nome'], 'preco': produto['preco']} for produto in produtos        
# ]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')

#adicionando 5% no preço de cada novo produto
print()
novos_produtos = [
    #isso ganha 5%
    {**produto, 'preco': produto['preco'] * 1.05}
    # se o produto for maior do que 20, senão é o mesmo preço
    if produto['preco'] > 20 else {**produto}
    for produto in produtos        
]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')






























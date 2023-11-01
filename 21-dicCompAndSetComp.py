# produto = {
#     'nome': 'caneta',
#     'preco': 2.5,
#     'marca': 'monblank',
# }

# print(*produto)
# print()
# print(produto)
# print()

# for chave, valor in produto.items():
#     print(chave, valor)
# print()
# dc = {
#    chave: valor 
#    for chave, valor 
#    in produto.items()
# }
# print('\ndc')
# for c, v in dc.items():
#     print(c, v)

# gerando um set com list comprehension

s1 = {2 ** i for i in range(1,11,1)}

print(s1)


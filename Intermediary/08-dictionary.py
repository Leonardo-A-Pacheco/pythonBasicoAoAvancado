# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Leonardo',
#     'sobrenome': 'Pacheco',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='leonardo', sobrenome='Pacheco')
# pessoa = {
#     'nome': 'leonardo',
#     'sobrenome': 'pacheco',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
# }
# # print(pessoa, type(pessoa))
# print(pessoa['nome'])
# print(pessoa['sobrenome'])

# print()

# for chave in pessoa:
#     print(chave, pessoa[chave])

# print(pessoa['endereços'])

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'leonardo',
    'sobrenome': 'pacheco',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
print()
print(len(pessoa))
print()
print(list(pessoa.keys()))
print()
print(list(pessoa.values()))
print()
print(list(pessoa.items()))
print()

for valor in pessoa.values():
    print(valor)
print()

for chave, valor in pessoa.items():
    print(chave, valor)
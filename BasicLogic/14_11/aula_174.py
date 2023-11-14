# combinações permutações e produtid ittertools
# combinação a ordem nao importa - iteravel + tamanho do grupo
# permutaçção a ordem ImportWarningproduto ordem importa e repete os valores UnicodeTranslateError
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')


pessoas = [
    'joão','joana','luiz','leticia',
]

camisetas = [
    ['preta','branca'],
    ['p','m','g'],
    ['masc', 'feme','unis'],
    ['algodao', 'poliester']
]
# #combinação não permitem repetição
# print_iter(combinations(pessoas,2))
# print()

# #permutações permitem repetição
# print_iter(permutations(pessoas,2))

#produto cartesiano combina todos com todos
print_iter(product(*camisetas))

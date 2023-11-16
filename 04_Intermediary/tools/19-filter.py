import pprint


lista = [ n for n in range(10) if n < 6]

print(lista)
#[0, 1, 2, 3, 4, 5]
print()
# assim como a complexidade de como montar as listas pde ser aumentada mais isso não é uma boa pratica, funções são mais adequadas para configurações complexas

duplo_for = []

for i in range(3):
    for j in range(3):
        duplo_for.append((i,j))
print(duplo_for)
print()
duplo_for_lc =[(x,y) 
               for x in range(3)
               for y in range(3)]
print(duplo_for_lc)

print('\n')

lst = [
    [(x, letra) for letra in 'leo']
    for x in range(3)
]
print(lst)







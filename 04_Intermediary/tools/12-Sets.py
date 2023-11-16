# Sets - Conjuntos em Python (tipo set)
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('leonardo')
s1 = set()  # vazio
s1 = {'Leonardo', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.

# l1 = [1,2,2,2,2,3,3,4,4,4,5,6,6,7,87,8]
# print(l1)
# # fazendo o typecasting
# l2 = set(l1)
# print(l2)
# # fazendo o typecasting
# l3 = list(l2)
# print(l3, type(l3))

#porem sets nao garantem a ordem dos dados



# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteraveis (for, in, not in)
# print(3 not in l1)

# for i in l2:
#     print(i)


# Métodos úteis:
# add, update, clear, discard

cs = set()
print(cs, type(cs))

# lança objeto
cs.add('nome')
print(cs)
print()

# lança objeto iteravel
cs.update('mãe')
print(cs)

# eliminando valor especifico do set
cs.discard('nome')
print(cs)
print()

 #limpando o set
cs.clear()
print(cs)





# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

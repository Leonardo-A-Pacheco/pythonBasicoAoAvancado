# somando duas listas
# considerando duas listas de inteiros ou floats lista a e lista b some valores nas listas retotnando uma nova lista com os valores somados

# se uma lista for maiort que a outra a soma so vai considerar o tamanho menor
    
# exemplo:
# lista a[1,2,3,4,5,6,7]
# lista b[1,2,3,4]

# lista soma = s,4,6,8
# exemplo:

a = [1,2,3,4,5,6,7]
b = [1,2,3,4]
s = []

for i in range(max(len(a),len(b))):
    if i < len(a) and i < len(b):
        s.append(a[i]+b[i])
    elif i < a[i]:
        s.append(a[i])
    else:
        s.append(b[i])

print(s)

#desempacotando, e atibuindo a soma desempacotada em s1
s1 = [x + y for x, y in zip(a, b)] 
print(s1)



# O problema é que zip só une as listas até o tamanho da menor lista (como proposto no exercício).

# Uma outra possibilidade é usar zip_longest para capturar os valores da lista maior.

# A ideia é a mesma, veja:

# from itertools import zip_longest
 
# lista_a = [10, 2, 3, 4, 5]
# lista_b = [12, 2, 3, 6, 50, 60, 70]
# lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
# print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]

# Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos capturar os valores restantes da lista maior, realizando contas, sem obter um erro em nosso programa.
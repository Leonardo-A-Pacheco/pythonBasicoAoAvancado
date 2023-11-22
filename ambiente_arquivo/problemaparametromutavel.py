def adiciona(nome, lista=None):
    if lista is None:
        lista=[]
    lista.append(nome)
    return lista

#inicializa a lista
l1 = adiciona('adolfo')
#executa a função
adiciona('beatriz',l1)
#caso a lista não seja definida retorna apenas o que ja foi feito
adiciona('carlos')

print(l1)



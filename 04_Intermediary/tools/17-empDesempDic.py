# empacotamento e desempacotamento de dicionarios
a, b = 1, 2
a, b = b, a

# print(a,b)

pessoa = {
    'nome': 'carla',
    'sobrenome': 'Silva'
}
(a1, a2), (b1, b2) = pessoa.items()

# print(a1,a2)
# print(b1,b2)

#cada valor é um item do dicionario
# for valor in pessoa.items():
#     print(valor)

#utlizando o desempacotamento fazemos

# for chave, valor in pessoa.items():
#     print(chave, valor)

# args e kwargs
# args ja vimos
# kwargs = keyword arguments (argumentos nomeados)

pessoa = {
    'nome': 'carla',
    'sobrenome': 'Silva'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.66
}
#para extrair valores de um dicionario usamos dois asteriscos {**}

pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

def mostra_arg_nomeados(*args, **kwargs):
    print('NAO NOMEADOS', args)

    for chave, valor in kwargs.items():
        print(chave,valor)

mostra_arg_nomeados(nome='joana', qlq=123) 
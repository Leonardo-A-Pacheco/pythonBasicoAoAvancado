# operação ternária (condicional de uma linha)
# <valor> <condição> else <outro valor>

# condicao = 1 == 0

# var = 'valor' if condicao else 'outro valor'

# print(var)

# outro exemplo

# se o digito for maior que 9 novodigito = 0, se digito = 9 então 9

digito = 10

novo_digito = digito if digito <= 9 else 0

print(novo_digito)

print('Valor' if False else 'Outro valor' if False else 'Fim')

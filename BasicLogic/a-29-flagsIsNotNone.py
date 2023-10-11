"""
Flag (Bandeira) - Marcar um local
None = Não valor ou nulo como em outras linguagens
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
percebemos no codigo abaixo que 
0 = False = None
"""
# variaveis globais
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True #variavel local if
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
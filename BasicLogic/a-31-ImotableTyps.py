"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
#string imutavel
string = 'leonardo pacheco'
# atribuição em outra variavel com a variavel decima
outra_variavel = f'{string[:8]}ABC{string[9:]}'

print(string)

print(outra_variavel)

print(string.zfill(20))
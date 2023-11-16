"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'periquita molhadinha'

#tamanho variavel
print(len(variavel))
print('-------------')

#por indice inicial
print(variavel[0:])
print(variavel[1:])
print(variavel[2:])
print('-------------')

#apenas posição
print(variavel[:0])
print(variavel[:1])
print(variavel[:2])
print('-------------')

#espaço entre indice inicio + posição 
print(variavel[0:3])
print(variavel[1:4])
print(variavel[2:5])
print('------------')

#por contando de tras para frente
print(variavel[:5:1])
print(variavel[:6:1])
print(variavel[:7:1])
print('-----------')

#iniciando de tras para frente
print(variavel[::-1])

print('-----------\n')

#começando do indice 0
#até o tamanho total
#passo ...
print(variavel[0:len(variavel):1])

print('-----------\n')

print(variavel[20:-(1+len(variavel)):-1])





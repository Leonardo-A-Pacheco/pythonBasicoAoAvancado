# Calculo do primeiro dígito do CPF
# CPF: 746.824.890-70
# Colete a soma dos 9 primeiros dígitos do CPF
# multiplicando cada um dos valores por uma
# contagem regressiva começando de 10
# Ex.:  746.824.890-70 (746824890)
#    10  9  8  7  6  5  4  3  2
# *  7   4  6  8  2  4  8  9  0
#    70  36 48 56 12 20 32 27 0
# Somar todos os resultados: 
# 70+36+48+56+12+20+32+27+0 = 301
# Multiplicar o resultado anterior por 10
# 301 * 10 = 3010
# Obter o resto da divisão da conta anterior por 11
# 3010 % 11 = 7
# Se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resultado é o valor da conta
# O primeiro dígito do CPF é 7
# testando cpfs
cpf = '746.824.890-70'
# cpf = '947.937.828-09'
# cpf = '351.288.863-10'

scpf = cpf.replace('.','')
scpf = scpf.replace('-','')

# print(scpf)

cpf_9 = []

for n in range((len(scpf)-2)):
    
    cpf_9.append(int(scpf[n]))
 
# print(cpf_9,type(cpf_9))

# for i in range (len(cpf_9)):
#     print(type(cpf_9[i]))

cpfx = []
j = 10

for i in range (len(cpf_9)):
    cpfx.append(cpf_9[i] * j)
    j -= 1

soma = 0

for i in range(len(cpfx)):
    soma += cpfx[i]

# print(cpfx)
soma = soma *10  
# print(soma)

result_n1 = soma % 11
#result_n1 mas se result_n1 falso então 0
result_n1 = result_n1 if result_n1 <= 9 else 0

print(f'resultado primeiro digito: {result_n1}')


# Calculo do segundo dígito do CPF
# CPF: 746.824.890-70
# Colete a soma dos 9 primeiros dígitos do CPF,
# MAIS O PRIMEIRO DIGITO,

# multiplicando cada um dos valores por uma
# contagem regressiva começando de 11
# Ex.:  746.824.890-70 (7468248907)
#    11 10  9  8  7  6  5  4  3  2
# *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
#    77 40 54 64 14 24 40 36  0 14

# Somar todos os resultados:
# 77+40+54+64+14+24+40+36+0+14 = 363
# Multiplicar o resultado anterior por 10
# 363 * 10 = 3630
# Obter o resto da divisão da conta anterior por 11
# 3630 % 11 = 0
# Se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resultado é o valor da conta

# O segundo dígito do CPF é 0

n2 = cpf_9
n2.append(result_n1)
# print(n2)
result_n2 = 0
j = 11
for i in range (len(n2)):
    result_n2 += n2[i] * j
    j -= 1 
result_n2 = (result_n2 * 10) % 11
result_n2 = result_n2 if result_n2 <= 9 else 0
print(f'resultado segundo digito: {result_n2}')

















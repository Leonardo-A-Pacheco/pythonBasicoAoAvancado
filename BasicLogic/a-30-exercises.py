# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.



# var = input('Escreva um número inteiro:')

# if not var.isdigit():
#     raise ValueError('Isso não é um número inteiro')

# try:
#     n = int(var)
#     if n % 2 == 0:
#         print('Número par')
#     else:
#         print('Número ímpar')
# except ValueError as e:
#     print(f'Erro: {e}')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# 1 pede a leitura
# 2 verifica se é um numero Inteiro
# 3 faz typecasting de hour para h como inteiro
# 4 enquanto ok == true faça leitura

# 1 pede a leitura
# 2 verifica se é um numero Inteiro
# 3 faz typecasting de minute para m como inteiro

# import datetime

# print(f'Dia e Hora Atual: {datetime.datetime.now()}\n')

# ok = False

# while not ok:
#     try:
#         entrada = input('Entre com a hora HH: ')
#         h = int(entrada)
#         if 0 <= h < 24:
#             # print(f'Hora informada: {h}')
#             ok = True
#         else:
#             print('Entrada inválida. Digite uma hora válida entre 00 e 23.\n')
#     except ValueError:
#         print('Entrada inválida. Digite uma hora válida HH (número inteiro).\n')

# ok = False
# entrada = None

# while ok == False:
#     try:
#         entrada = (input('entre com os minutos MM: '))
#         if entrada.isdigit():
#             m = int(entrada)
            
#             if -1 < m < 60:
#                 # print(f'Minuto informado: {m}\n\n')
#                 ok = True
#             else:
#                 print('Entrada inválida. Digite uma minuto entre 01 e 59.\n')
#         else:
#             print('Entrada inválida. Digite um minuto válido MM (número inteiro).\n')

#     except ValueError:
#         print('Entrada inválida. Digite um minuto válido MM (número inteiro).\n')

#     horario = {'hora': h, 'minuto': m}

#     print(f'\n\nHorário informado: {horario["hora"]}:{horario["minuto"]}')

#     if (1 <= horario["hora"] <=11) or \
#         (horario['hora'] == 12 and horario['minuto'] == 0):
#         print('bom dia')
    
#     elif (12 <= horario["hora"] <=17) or \
#         (horario['hora'] == 18 and horario['minuto'] == 0):
#         print('boa tarde')
    
    
#     elif (18 <= horario["hora"] <=23) or \
#         (horario['hora'] == 0 and horario['minuto'] == 0):
#         print('boa noite')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Entre com seu primeiro nome: ')

try:
    if nome.isalpha():
        print(f'your name have: {len(nome)} letters')
    else:
        raise ValueError
except ValueError:
    print('nome invalido')

if len(nome) < 4:
    tamanho = 'small'
elif 4 < len(nome) <= 6:
    tamanho = 'normal'
else:
    tamanho = 'big' 

print(f'your name is: {tamanho} ')


## ESCREVENDO EM COLUNA
# for letra in nome:
#     print(letra)

# for i in range(len(nome)):
#     print(nome[i])

# i = 0
# while i < len(nome):
#     print(nome[i])
#     i += 1

##ESCREVENDO EM LINHA
# print(nome)




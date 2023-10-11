# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

# var = input('Escreva um numero inteiro: ')

# if (var.isdigit()):
#     n = int(var)
#     if ((n % 2) == 0):
#         print('numero par')
#     else:
#         print('numero impar')
# else:
#     print('isso nao é um numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('digite a hora hh:mm')

momento = hora[0:2:]



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
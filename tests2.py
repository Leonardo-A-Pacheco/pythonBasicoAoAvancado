# import os
# import random

# certas = []

# def estado(erros):
#     if erros == 0:
#         print('           _________')
#         print('          |        |')
#         print('          |        ')
#         print('          |        ')
#         print('          |        ')
#         print('          |        ')
#         print('    ______|_____   \n')
    
#     elif erros == 1:
#         print('          _________')
#         print('          |        |')
#         print('          |        O')
#         print('          |        ')
#         print('          |        ')
#         print('          |        ')
#         print('    ______|_____   \n')
   
#         print('    E R R O - 1  !')

#     elif erros == 2:
#         print('          _________')
#         print('          |        |')
#         print('          |        O')
#         print('          |        |')
#         print('          |        ')
#         print('          |        ')
#         print('    ______|_____   \n')
    
#         print('    E R R O - 2  !')


#     elif erros == 3:
#         print('          _________')
#         print('          |        |')
#         print('          |        O')
#         print('          |       /|')
#         print('          |        ')
#         print('          |        ')
#         print('    ______|_____   \n')
    
#         print('    E R R O - 3  !')


#     elif erros == 4:
#         print('          _________')
#         print('          |        |')
#         print('          |        O')
#         print('          |       /|\ ')
#         print('          |        ')
#         print('          |        ')
#         print('    ______|_____   \n')
    
#         print('    E R R O - 4  !')


#     elif erros == 5:
#         print('          _________')
#         print('          |        |')
#         print('          |        O')
#         print('          |       /|>')
#         print('          |        | ')
#         print('          |         ')
#         print('    ______|_____   \n')
    
#         print('    E R R O - 5  !')


#     elif erros == 6:
#         print('          _________')
#         print('          |        |')
#         print('          |        O')
#         print('          |       <|\ ')
#         print('          |        |')
#         print('          |       /')
#         print('    ______|_____   \n')
    
#         print('    E R R O - 6  !')


#     elif erros == 7:
#         print('          _________')
#         print('          |        |')
#         print('          |        O')
#         print('          |       /|\  ')
#         print('          |        |')
#         print('          |       / \ ')
#         print('    ______|_____   \n')
        
#         print('    # E R R O - 7  !')
    
#         print('  V O C Ê   M O R R E U !!!')

# def clear():
#     return os.system('cls')

# def escolhe_palavra(p):
#    ok = random.randint(0,len(p))
#    return p[ok]

# def todas_letras_adivinhadas(palavra, certas):
#     for letra in palavra:
#         if letra not in certas:
#             return False
#     return True










# def game_forca():
#     p = ['abacate', 'copo', 'forca', 'registro', 
#          'cortador', 'uno', 'maionese', 'notebook', 'python']

#     palavra = escolhe_palavra(p)
#     fail = 0
#     acertos = ['_'] * len(palavra)
    
#     print('JOGO DA FORCA')
#     while ''.join(acertos) != palavra and fail < 7:
#         estado(fail)
#         print(f'Adivinhe a palavra abaixo: {"".join(acertos)}')
        
#         kick = input('Chute uma letra: ')
        
#         if kick in palavra:
#             for i, letra in enumerate(palavra):
#                 if letra == kick:
#                     acertos[i] = kick
#         else:
#             fail += 1
#             clear()

#     if ''.join(acertos) == palavra:
#         print(f'Você venceu, a palavra é: {palavra}')
#     else:
#         print('Você perdeu! A palavra era:', palavra)

# game_forca()









# # def apresentacao(**kwargs):
# #     for chave, valor in kwargs.items():
# #         print(f'{chave}: {valor}')

# # info = {'nome': 'Alice', 'idade': 30, 'cidade': 'Nova York'}
# # apresentacao(**info)  # Passa o dicionário como argumentos de palavra-chave



# # def soma(*args):
# #     resultado = 0
# #     for num in args:
# #         resultado += num
# #     return resultado

# # nums = (1, 2, 3, 4, 5)
# # resultado = soma(*nums)  # Desempacota a tupla em argumentos

# # print(resultado)


# # produtos = [
# #     {'nome': 'Produto 5', 'preco': 10.00, 'categoria': 1},
#     # {'nome': 'Produto 1', 'preco': 22.32, 'categoria': 2},
#     # {'nome': 'Produto 3', 'preco': 10.11 , 'categoria': 3},
#     # {'nome': 'Produto 2', 'preco': 105.87, 'categoria': 4},
#     # {'nome': 'Produto 4', 'preco': 69.90}, 'categoria': 5},
# # ]

# # print(produtos)



# # ldl = [
# #     [10, 2, 3, 4, 5, 6, 7, 3, 2, 10],
# #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# # ]

# # for i in range(len(ldl)):
# #         print()
# #         t = len(ldl[i])
# #         for e in range(t // 2):
# #             esquerda = ldl[i][e]
# #             direita = ldl[i][-1 - e]
# #             print(f"{esquerda} com {direita}")

# # # a = 'a) banana'
# # # print(a[:1])

# # perguntas = {
# #         #chave     : valor
# #         'pergunta': 'How are you from?',

# #         #chave      valores
# #         'opcoes': ['a) como é o seu nome?', 'b) que horas são agora?', 'c) Poneis são azuis?', 'd) De onde você é?', 'e) Isso é uma bicicleta?'],

# #         #chave     : valor
# #         'resposta': 'd) De onde você é?',
# #     }


# # print(perguntas['resposta'][0])


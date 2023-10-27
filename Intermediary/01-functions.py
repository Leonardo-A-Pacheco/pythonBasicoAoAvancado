# funções podem receber valores como parametros para retornar um valor especifico apos o processamento, por padrão funçoes retornam None

# def funcao():
#     print('resultado processamento')
#     print('resultado processamento')
#     print('resultado processamento')

# funcao()

# # função com parametros
# def funcao_1(a, b, c):
#     print(a, b, c)
    
# #chamando a função com argumentos
# funcao_1(1, 2, 3)

# def saudacao(nome):
#     print(f'ola {nome} welcome!\n')

# saudacao('leonardo')
# saudacao('moly')
# saudacao('polaco')
# saudacao('rayka')
# saudacao('Brown')
# #criando valor padrão caso argumento nao seja passado
# def saudacao(nome='sem nome'):
#     print(f'ola {nome} welcome!\n')

# saudacao()

# argumentos nomeados e nao nomeados em funçoes python, argumento nomeado tem nome com sinal de igual argumento nao nomeado recebe apenas o argumento valor
#definição da função
# def soma (x=0, y=0):
#     # print(x + y)
#     print(f'{x=} + y={y}','|','x + y =', x + y)

# #endereço do nome da função
# # print(soma)

# #imprimindo a função que ja imprime por padrão retorna none
# # print(soma(1,2))
# #argumento posicional 
# soma(1,2)

# #nomeando os argumentos para apontar para os paramentros
# soma(y=3,x=1)

#todo parametro que tem um valor padrão todos os outros que vierem apos ele devem ter tambem um valor padrão

def soma(x,y,z=None):
    #se z não for vazio faça
    if z is not None:
        print(f'{x=} {y=} {z=} |', x + y + z)
    #senão faça
    else:
        print(f'{x=} {y=} |', x + y)
    print()
soma(1,2)
soma(1,2,3)

soma(z=1,x=2,y=3)

















# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com 
# erros de índices inexistentes na lista.
import os
lista = []
while True:
    op = input('Escolha uma opção:'
            '\n[i] para inserir'
            '\n[d] para apagar'
            '\n[v] para listar'
            '\n[l] para limpar tela'
            '\n[s] para sair\n')

    op = op.lower()  # Converte para minúsculas

    ok = len(op) == 1 and op.isalpha() 

    if ok and op == 'i':
        # print('Você escolheu opção "i" para inserir.')
        add = input('entre com produto ')
        lista.append(add) 
        os.system('cls')
    elif ok and op == 'd':
        os.system('cls')
        print('indice  -  produto')
        for indice, produto in enumerate(lista):
            print(f'{indice}  -  {produto}')
        delete = int(input('escolha algum dos indices acima para deletar '))
        if 0 <= delete <= len(lista):
            lista.pop(delete)
        else:
            print('invalido') 

    

    elif ok and op == 'v':
        os.system('cls')
        print('Você escolheu opção "v" para visualizar.')

        for produto in (lista):
            print(f'{produto}')
      
    elif ok and op == 's':
        print('Você escolheu opção "s" para sair.')
        break
    elif ok and op == 'l':
        # print('Você escolheu opção "s" para sair.')
        os.system('cls')
    else:
        print('Opção inválida!')
        os.system('cls')

    # os.system('cls')

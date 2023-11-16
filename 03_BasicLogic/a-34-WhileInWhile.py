"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1
# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha = }  {coluna = }')
#         coluna += 1
#     linha += 1
#     print('\n')


# print('Acabou')

# linha = 1
# while linha <= 5:
#     coluna = 1 # resseta a coluna do segundo while em 1
#     while coluna <= 5:
#         print(f'{linha},{coluna}', end=' ')
#         coluna += 1
#     print(' \n')
#     linha += 1 # passa para proxima linha

i = j = 5

row = 1

while row <= i:
    clm = 1

    while clm <= j:

        print(f'({row},{clm})',end=' ')
        clm += 1
        
    row += 1
    print('\n')

    

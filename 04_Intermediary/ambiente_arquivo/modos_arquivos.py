# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)


caminho_arquivo = r'D:\\• DEV •\\pythonBasicoAoAvancado\\04_Intermediary\\VirtualAmbient\\'
caminho_arquivo += 'modos.txt'

#o modo w apaga tudo e começa do 0
# with open(caminho_arquivo, 'w') as arquivo:
#     ...
#o modo w apaga tudo e começa do 0
with open(caminho_arquivo, 'a+') as arquivo:
    arquivo.write('inserindo no fim com a+')

with open(caminho_arquivo, 'a+') as arquivo:
    arquivo.write('\ninserindo MAIS UM POUCO')

with open(caminho_arquivo, 'a+') as arquivo:
    arquivo.write('\nverificando a codificação de caracteres')
#caminho do arquivo / modo de operação / codificação utilizada
with open(caminho_arquivo, 'a+', encoding='utf-8') as arquivo:
    arquivo.write('\nverificando a codificação apos encoding no with open')

# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('linha1\n')
#     arquivo.write('linha2\n')

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('linha 1\n')
#     arquivo.write('linha 2\n')
#     arquivo.writelines(
#         ('linha 3\n', 'linha 4\n')
#     )
#     arquivo.seek(0,0)
#     print(arquivo.read())
    
#     print('lendo')
#     arquivo.seek(0,0)
#     print(arquivo.readline())
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
    
#     print('readlines')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('-------------------')

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())
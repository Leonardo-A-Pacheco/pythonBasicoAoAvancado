
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

caminho_arquivo = r'D:\\• DEV •\\pythonBasicoAoAvancado\\04_Intermediary\\VirtualAmbient\\'
caminho_arquivo += 'teste.txt'

# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('linha1\n')
#     arquivo.write('linha2\n')

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'linha 4\n')
    )
    arquivo.seek(0,0)
    print(arquivo.read())
    
    print('lendo')
    arquivo.seek(0,0)
    print(arquivo.readline())
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    
    print('readlines')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('-------------------')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
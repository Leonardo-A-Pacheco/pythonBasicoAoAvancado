import os

# caminho_arquivo = r'D:\\• DEV •\\pythonBasicoAoAvancado\\04_Intermediary\\VirtualAmbient\\'
# caminho_arquivo += 'temp.txt'



# #caminho do arquivo / modo de operação / codificação utilizada
# with open(caminho_arquivo, 'a+', encoding='utf-8') as arquivo:
#     arquivo.write('\nverificando a codificação apos encoding no with open')

# os.remove(caminho_arquivo)

caminho_arquivo = r'D:\\• DEV •\\pythonBasicoAoAvancado\\04_Intermediary\\VirtualAmbient\\firstambient\\'

ca = caminho_arquivo

caminho_arquivo += 'renomear.txt'

with open(caminho_arquivo, 'a+', encoding='utf-8') as arquivo:
    arquivo.write('\nverificando a codificação apos encoding no with open')

os.rename(ca, 'renomeado.txt')




















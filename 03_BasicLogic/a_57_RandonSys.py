import random
import os
import sys

# Gerando um número inteiro aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)
print(f'Número aleatório: {numero_aleatorio}')

# Escolhendo um elemento aleatório de uma lista
lista_de_frutas = ['maçã', 'banana', 'laranja', 'uva', 'morango']
fruta_aleatoria = random.choice(lista_de_frutas)
print(f'Fruta aleatória: {fruta_aleatoria}')

print('---------------------------')

# Obtendo o diretório de trabalho atual
diretorio_atual = os.getcwd()
print(f'Diretório atual: {diretorio_atual}')

# Listando arquivos em um diretório
arquivos = os.listdir(diretorio_atual)
print('Arquivos no diretório atual:')
for arquivo in arquivos:
    print(arquivo)

# Verificando se um arquivo existe
arquivo = 'exemplo.txt'
if os.path.exists(arquivo):
    print(f'O arquivo {arquivo} existe.')
else:
    print(f'O arquivo {arquivo} não existe.')


# finaliza o programa
sys.exit()

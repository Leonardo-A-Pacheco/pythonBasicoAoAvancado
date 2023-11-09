import os
import random

certas = []

def estado(erros):
    if erros == 0:
        print('           _________')
        print('          |        |')
        print('          |        ')
        print('          |        ')
        print('          |        ')
        print('          |        ')
        print('    ______|_____   \n')
    
    elif erros == 1:
        print('          _________')
        print('          |        |')
        print('          |        O')
        print('          |        ')
        print('          |        ')
        print('          |        ')
        print('    ______|_____   \n')
   
        print('    E R R O - 1  !')

    elif erros == 2:
        print('          _________')
        print('          |        |')
        print('          |        O')
        print('          |        |')
        print('          |        ')
        print('          |        ')
        print('    ______|_____   \n')
    
        print('    E R R O - 2  !')


    elif erros == 3:
        print('          _________')
        print('          |        |')
        print('          |        O')
        print('          |       /|')
        print('          |        ')
        print('          |        ')
        print('    ______|_____   \n')
    
        print('    E R R O - 3  !')


    elif erros == 4:
        print('          _________')
        print('          |        |')
        print('          |        O')
        print('          |       /|\ ')
        print('          |        ')
        print('          |        ')
        print('    ______|_____   \n')
    
        print('    E R R O - 4  !')


    elif erros == 5:
        print('          _________')
        print('          |        |')
        print('          |        O')
        print('          |       /|>')
        print('          |        | ')
        print('          |         ')
        print('    ______|_____   \n')
    
        print('    E R R O - 5  !')


    elif erros == 6:
        print('          _________')
        print('          |        |')
        print('          |        O')
        print('          |       <|\ ')
        print('          |        |')
        print('          |       /')
        print('    ______|_____   \n')
    
        print('    E R R O - 6  !')


    elif erros == 7:
        print('          _________')
        print('          |        |')
        print('          |        O')
        print('          |       /|\  ')
        print('          |        |')
        print('          |       / \ ')
        print('    ______|_____   \n')
        
        print('    # E R R O - 7  !')
    
        print('  V O C Ê   M O R R E U !!!')

def clear():
    return os.system('cls')

def escolhe_palavra(p):
   ok = random.randint(0,len(p))
   return p[ok]

def todas_letras_adivinhadas(palavra, certas):
    for letra in palavra:
        if letra not in certas:
            return False
    return True

p = ['abacate', 'copo', 'forca', 'registro', 
    'cortador', 'uno','maionese', 'notebook', 'python']
palavra = escolhe_palavra(p)


def game_forca():
    # limpa_tela()
    
    fail = 0
    
    print('JOGO DA FORCA')
    while not todas_letras_adivinhadas(palavra, certas) and fail < 7:
            estado(fail)

            print('Adivinhe a palavra abaixo:')
            print(palavra)
            for _ in range(len(palavra)):
                print(f'( _ )',end='')
            print()

            kick = ''
            while len(kick) != 1:
                kick = input('chute apenas uma letra ')

            if kick in palavra:
                for i in palavra:
                    if i == kick:
                        print(f'( {i} )',end='')   
                        certas.append(kick)
                    # else:
                    #     print(f'( {certas} )',end='')
            else:
                fail += 1
                clear()
            print()


game_forca()

print(f'voce venceu, a palavra é: {palavra}')
# Faça um jogo para o usuário adivinhar qual
# a palavra secreta.
# - Você vai propor uma palavra secreta
# qualquer e vai dar a possibilidade para
# o usuário digitar apenas uma letra.
# - Quando o usuário digitar uma letra, você 
# vai conferir se a letra digitada está
# na palavra secreta.
#     - Se a letra digitada estiver na
#     palavra secreta; exiba a letra;
#     - Se a letra digitada não estiver
#     na palavra secreta; exiba *.
# Faça a contagem de tentativas do seu
# usuário.

import os
p = 'leonardo'
p = p.lower()
d = ''
ok = ''
t = 0
while True:

    d = input('digite uma letra: ')
    t += 1

    if len(d) > 1:
        print('digite apenas uma letra')
        continue
    if d in p:
        ok += d
    
    p_ok = ''
    for i in p:
        if i in ok:
            p_ok += i
        else:
            p_ok += '*'

    print(f'palavra formada: {p_ok}')
    if p_ok == p:
        os.system('cls')
        print(f'palavra formada: {p_ok}')
        print(f'numero tentativas: {t}')
        print('voce venceu')
        ok = ''
        t = 0
        break




















# while/else 
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print(f'Não encontrei um espaço na string. ')
print(f'Fora do while.  ')

#se houver um break antes o else nao é executado
#se não houver ele é sempre executado!

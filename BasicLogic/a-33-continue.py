contador = 0


while contador < 10:
    
    contador += 1
    
    if contador == 6:
        print(f'condição continue')
        continue
    
    print(contador)

    if contador == 9:
        print('condição break')
        break
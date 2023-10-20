while True:

    n1 = input('Digite o n1: ')
    op = input('Digite o operador: ')
    n2 = input('Digite o n2: ')
    ok = None
    n1_float = 0 
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        ok = True
    except:
        ok = None
    
    if ok == None:
        print('Um ou ambos numeros são invalidos ')
        continue

    op_ok = '+-*/'

    if op not in op_ok:
        print('operador invalido ')
        continue
    
    if len(op) > 1:
        print('digite apenas um operador ')
        continue

    print('Realizando seu cauculo confira abaixo: ')

    if op == '+':
       print(f'{n1_float} + {n2_float} =',n1_float + n2_float)

    elif op == '-':
       print(f'{n1_float} - {n2_float} =',n1_float - n2_float)
    
    elif op == '*':
       print(f'{n1_float} * {n2_float} =',n1_float * n2_float)
    
    elif op == '/':
       print(f'{n1_float} / {n2_float} =',n1_float / n2_float)
    
    else:
        print('algo de errado nao esta certo')



    sair = input('quer sair digite [s] ')
    sair = sair.lower().startswith('s') 
    #coloca tudo em minuscula
    #qualquer coisa que comece com s
    if sair is True:
        break


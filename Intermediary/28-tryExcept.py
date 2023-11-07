# try:
#     a=12
#     b='0'
#     # b=0
#     print('linha1')
#     c=a/b
#     print('linha2')
# except ZeroDivisionError:
#     print('divisão por zero')
#     print('linha2')
# except NameError:
#     print('b naão esta definido')
# except (TypeError, IndexError) as error:
#     print('type error + index error')
#     print('MSG:', error)
#     print('nome:', error.__class__.__name__)
# except Exception:
#     print('erro desconhecido')

# print('continue')

try:
     5/0
except ZeroDivisionError:
    print('divisão por zero')
else:
    print('nao deu erro')
finally:
    print('fechar arquivo')
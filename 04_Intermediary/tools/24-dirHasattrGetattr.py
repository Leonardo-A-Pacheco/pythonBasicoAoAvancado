# dir, hasattr getattr

string = 'leonardo'

print(string)

# exibindo os metodos possiveis para a string
print(dir(string))

# verificando se o metodo solicitado existe
if hasattr(string, 'upper'):
    print('existe')
else:
    print('NAO existe')

# alojando metodo na vairavel

metodo= 'upper'
print(metodo)

print(getattr(string,metodo)())


# print(string.metodo()())
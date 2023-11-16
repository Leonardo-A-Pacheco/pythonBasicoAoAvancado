print(f'exercicio guiado com while') 
#colocar um esterisco antes e depois de cada letra de uma string
# *l*e*o*n*a*r*d*o*

i=0
string = 'leonardo pacheco'
processado = ''

while i < len(string):
    letra = string[i]
    processado += f'*{letra}'
    i += 1

processado += '*'
print(processado)

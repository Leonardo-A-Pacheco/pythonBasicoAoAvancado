nome = 'leo'
altura = 1.80
idade = 77
peso = 111.1

imc = (float(peso) / (float(altura) * float(altura)))

print('seu imc é',imc) 

# . . . é um placeholder utilizado para marcar um local que necessita
#de atenção com um novo codigo

#falando sobre f strings:

string_a = '\nnome altura idade peso imc\n'
print(string_a)


string_b = f'\n{nome} altura {idade} peso {imc:.2f}\n'
print(string_b)


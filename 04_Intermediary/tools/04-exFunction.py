# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    m = 1
    for i in args:
        m *= i
    return m

var = mult(2,4,6,8)

print(var)
print('----------------\n')
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(n=None):
    if (n is None):
        return 'sem dados'
    elif (n % 2 == 0):
        return 'par'

    return 'impar'

print(par_impar(3))
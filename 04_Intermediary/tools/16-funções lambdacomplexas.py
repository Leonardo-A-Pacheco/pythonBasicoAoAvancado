def executa(fx, *args):
    return fx(*args)



def soma(x,y):
    return x + y

# desenvolvendo uma função lambda para substituir a função soma acima:

# print(
#     # utilizando a função executa recebendo a função e n argumentos
#     executa(
#         lambda x , y: x + y,
#         2, 3
#     )
# ) 

#função composta simples de 2 niveis
def cria_multiplicador(multiplicador):
    def multiplica(n):
        return n  * multiplicador
    return multiplica

#função composta com 3 niveis lambda
duplica = executa(lambda mult: lambda n: n * mult, 2)

print(duplica(2))

print(
    executa(
        lambda *args : sum(args), 1,2,3,4,5,6,7
    )
)
# decoradores com parametros
def decoradora(func):
    print('decoradora 1')
    def interna (*args, **kwargs):
        print('interna')
        res = func(*args, **kwargs)
        return res
    return interna

@decoradora
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

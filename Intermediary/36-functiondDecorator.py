# funções decoradoras e decoradores
# decorar = adicionar/remover/restringir/alternar
# funções decoradoras são funções que decoram outras funções
# decoradoras são usadas para fazer o pthon
# usar funções decoradoras em outras funções


def cria_funcao(fx):
    def fx_decoradora(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        result = fx(*args, **kwargs)  # Correção: Usar fx em vez de func
        print(f'O seu resultado foi {result}.')
        print('Ok, agora você foi decorada')
        return result
    return fx_decoradora

def inverte_string(string):
    return string[::-1]

i = inverte_string('leonardo')
print(i)

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser string')

inv_str_check_param = cria_funcao(inverte_string)
invertida = inv_str_check_param('123')


print(invertida)


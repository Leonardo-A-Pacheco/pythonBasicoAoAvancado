# metodos estaticos estaticmethod
# sãi inuteis em python
# metodos estaticos são metodos que estão dentro da classe mas nao tem acesso ao self nem ao cls.
# em resumo são funções que existem dentro da classe

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('oi', args, kwargs)

c1 = Classe()

c1.funcao_que_esta_na_classe(1,2,3)

Classe.funcao_que_esta_na_classe(nomeado='um')
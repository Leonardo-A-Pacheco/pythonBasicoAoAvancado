# # Módulos padrão do Python (import, from, as e *)
# # https://docs.python.org/3/py-modindex.html
# # inteiro - import nome_modulo
# # Vantagens: você tem o namespace do módulo
# # Desvantagens: nomes grandes
# # import sys

# # platform = 'A MINHA'
# # print(sys.platform)
# # print(platform)

# # partes - from nome_modulo import objeto1, objeto2
# # Vantagens: nomes pequenos
# # Desvantagens: Sem o namespace do módulo
# # from sys import exit, platform

# # print(platform)

# # alias 1 - import nome_modulo as apelido
# # import sys as s

# # sys = 'alguma coisa'
# # print(s.platform)
# # print(sys)


# # alias 2 - from nome_modulo import objeto as apelido
# # from sys import exit as ex
# # from sys import platform as pf

# # print(pf)

# # Vantagens: você pode reservar nomes para seu código
# # Desvantagens: pode ficar fora do padrão da linguagem

# # má prática - from nome_modulo import *
# # Vantagens: importa tudo de um módulo
# # Desvantagens: importa tudo de um módulo
# # from sys import exit, platform

# # print(platform)
# # exit()

# entendendo os seus proprios modelos python
# o primeiro modulo executado se chama __main__
# voce pode importar outro modulo inteiro ou parte do Modulo
# o pyton conhece a pasta onde o main está e as pastas abaixo dele
# ele nao reconhece pastas e modulos acima do __main__ por padrão
# o python conhece todos os modulos e pacotes presentes nos caminhos sys.path

print('este modulo se chama: ',__name__)
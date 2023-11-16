# entendendo os seus proprios modelos python
# o primeiro modulo executado se chama __main__
# voce pode importar outro modulo inteiro ou parte do Modulo
# o pyton conhece a pasta onde o main está e as pastas abaixo dele
# ele nao reconhece pastas e modulos acima do __main__ por padrão
# o python conhece todos os modulos e pacotes presentes nos caminhos sys.path

import moduloM_31

# caso seja preciso recarregar o modulo usase import importlib

print('este modulo se chama: ',__name__)

print(moduloM_31.variavel_modulo)

print(moduloM_31.fx_modulo(2,3))
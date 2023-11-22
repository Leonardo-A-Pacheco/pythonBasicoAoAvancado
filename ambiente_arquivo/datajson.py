import json

##json nao aceitaset {1,2,3,a}
##criando json
# pessoa = {
#     'nome': 'Leonardo ',
#     'sobrenome': 'Pacheco',
#     'enderecos': [
#         {'rua': 'araçatuba', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('nome_arquivo.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo,
#         ensure_ascii=False,
#         indent=2,
#         )



##as tuplas voltam sendo uma lista
##dragando json
with open('nome_arquivo.json', 'r', encoding='utf8') as arquivo:
    pessoadojson = json.load(arquivo)

print(pessoadojson)

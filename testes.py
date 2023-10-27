def cria_fx(n):
    def mult_fx(x):
        return x * n
    return mult_fx

dp = cria_fx(2)
tp = cria_fx(3)
qd = cria_fx(4)

valor = 5  # Substitua pelo valor que deseja multiplicar

print(f'Duplicado: {dp(valor)}\nTriplicado: {tp(valor)}\nQuadruplicado: {qd(valor)}')


# # Inicialização da flag
# encontrou_erro = False

# # Loop para processar uma lista
# for item in lista_de_itens:
#     if item.contem_erro():
#         encontrou_erro = True
#         break  # Sai do loop se encontrar um erro

# # Verificando a flag para tomar decisões
# if encontrou_erro:
#     print("Erros foram encontrados durante o processamento.")
# else:
#     print("Nenhum erro foi encontrado.")
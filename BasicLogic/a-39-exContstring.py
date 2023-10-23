#qual letra apareceu mais vezes na frase
string = 'aaaa bbbb ccccc dddddd eeeeeee' #30 caracteres
i = 0
soma = 0
# while i < len(string):
#     # print(f' {string.count(string[i])}\n')
#     a = string[i]
#     if string[i] == ' ':
#         i += 1
#         continue
#     c = string.count(a)
#     i += 1
#     print(f'letra:{a} aparece:{c}\n')


# #contando quantas letras diferentes tem:
# while i <= len(string):
#     soma = string.count(string[i])
#     print(soma)
#     i += 1
# print()


# qtd = 0 
# qtdrange = 0
# print(string.count(''))

# for i in string:
#     qtd += 1
# print(f'qtd = {qtd}')

# for i in range(0,len(string),1):
#     qtdrange += 1
# print(f'qtdrange = {qtdrange}') 


# # 1 criando um conjunto 
# # 2 passando cada caractere verificando se é texto
# # 3 adicionando  caracter no conjunto
# # 4 atribuindo qtd de letras diferentes no cunjunto
# # 5 exibindo quantas letras diferentes sem espaço tem na variavel sem espaços

# letras = set()

# for caractere in string:
#     if caractere.isalpha():
#         letras.add(caractere)

# quantidade_letras_diferentes = len(letras)
# print(f'Quantidade de letras diferentes na string (sem espaços): {quantidade_letras_diferentes}')

# print(letras)

#removendo espaços da string
texto = string.replace(' ', '')  # Remove os espaços
contlet = {}  # Dicionário para contar as letras

for i in texto:
    if i.isalpha():
        if i in contlet:
            contlet[i] += 1
        else:
            contlet[i] = 1

for letra, quantidade in contlet.items():
    print(f"A letra '{letra}' aparece {quantidade} vezes na string.")




"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('digite seu nome: ')
idade = input('digite seu idade: ')

if nome and idade:

    print(f'seu nome é: {nome}')

    # nome_invertido = nome[::-1]
    # print(f'seu nome invertido é: {nome_invertido}')
    # ou assim

    print(f'seu nome invertido eh: {nome[len(nome):-(1+len(nome)):-1]}')
    
    esp = nome.count(' ')
    
    if esp:
        print(f'seu nome tem {esp} espaços')
    else:
        print(f'seu nome não contem espaços')

    print(f' seu nome {nome} tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é: {nome[0]}')
    print(f'a ultima letra do seu nome é: {nome[len(nome)-1]}')
else:
    print('faltam dados a digitar')
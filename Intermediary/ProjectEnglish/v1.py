import random

# Lista de dicionários com palavras em português e suas traduções em inglês
dicionarios = [
    {"cachorro": "dog"},
    {"gato": "cat"},
    {"computador": "computer"},
    {"mesa": "table"},
    {"carro": "car"}
]

# Embaralha a ordem das palavras na lista de dicionários
random.shuffle(dicionarios)

# Loop para o jogo
for dicionario in dicionarios:
    for chave, valor in dicionario.items():
        # Exibir a palavra em português
        print(f"Traduza a palavra em português: {chave}")
        
        # Solicitar a tradução em inglês do usuário
        entrada_usuario = input("Sua resposta: ").lower()  # Ignora maiúsculas/minúsculas

        # Verificar se a entrada do usuário está correta
        if entrada_usuario == valor.lower():
            print("Correto! Próxima palavra.\n")
        else:
            print(f"Incorreto. A resposta correta é: {valor}\n")

print("Fim do jogo.")

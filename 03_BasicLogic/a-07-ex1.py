#entre com os dados de cada variavel
import datetime

ano_atual = datetime.datetime.now().year

# print(ano_atual)

nome = input(f"digite o nome ")
sobrenome = input("digite o sobrenome ")
anonascimento = input("digite o anonascimento ")
idade = ano_atual - int(anonascimento)
maiordeidade = input("digite o maiordeidade ")
altura = input("digite o altura ")

print("nome",nome)
print("sobrenome",sobrenome)
print("idade",idade)
print("anonascimento",anonascimento)
print("maiordeidade",maiordeidade)
print("altura",altura)
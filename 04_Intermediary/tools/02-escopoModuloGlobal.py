# escopo de funções em python
# escopo quer dizer onde aquele codigo pode atingir
# existe escopo global e locals
# o escopo global é o escopo onde todo codigo é alcançavel
# o escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
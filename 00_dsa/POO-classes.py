class Livro():
    def __init__(self):
        self.titulo = 'titulo do livro'
        self.isbn = 123134345
        # print('construtor chamado para criar o objeto dessa classe')
    

    def Imprime(self):
        print(f'livro: {self.titulo} ISBN:{self.isbn}')

l = Livro()

print(type(l))
print(l.titulo)
print(l.isbn)

l.Imprime()



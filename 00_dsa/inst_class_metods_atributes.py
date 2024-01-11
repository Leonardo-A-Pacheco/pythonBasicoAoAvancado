class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        # print('construtor chamado para criar o objeto dessa classe')

    def Imprime(self):
        print(f'livro: {self.titulo} ISBN:{self.isbn}')


l2 = Livro('bananas de pijamas', 124123)


l2.Imprime()
import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome (self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome


    @property
    def idade (self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name} {attrs}'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__=='__main__':
    c1 = Cliente('leonardo', 55)
    c1.conta = contas.ContaCorrente(299, 64714, 0, 1000)
    print()
    print(c1)
    print(c1.conta)

    c2 = Cliente('julia', 22)
    c2.conta = contas.ContaPoupanca(292, 12345, 12)
    print()
    print(c2)
    print(c2.conta)


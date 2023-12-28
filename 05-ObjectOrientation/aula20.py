# # super() e a sobreposição de membros - Python Orientado a Objetos
# # Classe principal (Pessoa)
# #   -> super class, base class, parent class
# # Classes filhas (Cliente)
# #   -> sub class, child class, derived class
# # class MinhaString(str):
# #     def upper(self):
# #         print('CHAMOU UPPER')
# #         retorno = super(MinhaString, self).upper()
# #         print('DEPOIS DO UPPER')
# #         return retorno

# class A:
#     atributo_a = 'valor a'

#     def metodo(self):
#         print('A')

# class B(A):
#     atributo_b = 'valor b'

#     def metodo(self):
#         # super().metodo()
#         print('B')

# class C(B):
#     atributo_c = 'valor c'

#     def metodo(self):
#         super(B, self).metodo()
#         super().metodo()
#         print('C')

# # print(C.mro())
# # print(B.mro())
# # print(A.mro())



# #nesse caso só fuincina o a
# # a = A()
# # print(a.atributo_a)
# # # print(a.atributo_b)
# # # print(a.atributo_c)

# # print()
# # #nesse caso só fuincina o a e b
# # b = B()
# # print(b.atributo_a)
# # print(b.atributo_b)
# # # print(b.atributo_c)

# # print()
# # #nesse caso só fuincina o a e b e c
# # c = C()
# # print(c.atributo_a)
# # print(c.atributo_b)
# # print(c.atributo_c)
# # c.metodo()

# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self):
        # super().metodo()  # B
        # super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        A.metodo(self)
        B.metodo(self)
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()




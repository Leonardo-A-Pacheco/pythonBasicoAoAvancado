# introdução as generator functions

# def generator(n=0):
#     yield 1
#     print('continuando...')
#     yield 2
#     print('mais uma...')
#     yield 3
#     print('proxima...')
#     yield 4
#     print('VOU TERMINAR...')
#     return 'acabou'

# gen = generator(n=0)

# for n in gen:
#     print(n)

def generator(n=0, max=10):
    while True:
        yield n
        n += 1

        if n > max:
            return

gen = generator(max= 33)

for n in gen:
    print(n)

# fale sobre dir
# fale sobre hasattr
# fale sobre getattr
# fale sobre iterable iterators
# fale sobre generator













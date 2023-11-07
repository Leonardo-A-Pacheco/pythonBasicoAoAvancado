def gen1():
    yield 1
    yield 22
    yield 3

def gen2():
    yield 4
    yield 55
    yield 6

def gen3():
    yield 7
    yield 88
    yield 999

def genx(gen):
    yield from gen()
    yield 'genx'
    yield 'executando como função composta'

def gen_chain():
    yield from gen1()
    yield from gen2()
    yield from gen3()

# g = gen_chain()
# executando de dentro para fora
g = genx(gen2)

for i in g:
    print(i)

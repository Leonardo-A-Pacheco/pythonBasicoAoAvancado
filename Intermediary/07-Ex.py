# crie funções que duplicam triplicam e quadruplicam o numero recebido como parametro

n = 2

def cria_fx(m):
  def mult_fx(n):
    return m * n 
  return mult_fx

dp = cria_fx(2)
tp = cria_fx(3)
qd = cria_fx(4)


print(f'duplicado: {dp(n)}\
    \ntriplicado: {tp(n)}\
    \nquadruplicado: {qd(n)}')
"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 69  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 59  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega
    
print(f'Velocidade atual do carro: {velocidade}')
print(f'trecho KM : {local_carro}')

multado = (velocidade > RADAR_1) and \
    (local_carro >= LOCAL_1 - RADAR_RANGE) and \
        (local_carro <= LOCAL_1 + RADAR_RANGE)

if multado:
    print('carro foi multado')


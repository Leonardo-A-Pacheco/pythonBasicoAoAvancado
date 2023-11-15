# fatorial

def fat(n):
    if n > 0:
        return n * fat(n-1)
    elif(n == 0):
        return 1
 
n = int(input('entre com o numero: '))

print(fat(n))



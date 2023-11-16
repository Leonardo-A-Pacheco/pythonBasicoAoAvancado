string = 'leonardo'

# l e o n a r d o

# 0 1 2 3 4 5 6 8

print (f'{len(string)} é o tamanho da string\n')

for i in range(len(string)):

    print(f"posição {i} : {string[i]}")


print('\n-----------\n')

#sentido normal
print(f'posição 4 {string[4]}\n')

#de tras para frente
print(f'posição -5 {string[-5]}\n')

print('leo' in string)

print('pacheco\n' in string)

print('nar' not in string)










  
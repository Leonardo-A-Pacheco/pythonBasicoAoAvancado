print('When you are bored, draw a picture on the backend')
pine ={
    'l1': '     *',
    'l2': '     ##',
    'l3': '    ####',
    'l4': '   ######',
    'l5': '  ########',
    'l6': ' ##########',
    'l7': '############',
    'l8': '     ##',
    'l9': '     ##',
    'l10': '     ##',
}

for i in pine:
    print(pine[i])

print()

smiley = {
    'eyes': ':)',
    'nose': '',
    'mouth': 'D'
}

for i in range(10):
    print(' ' * (10 - i) + smiley['eyes'] + ' ' * (2 * i) + smiley['mouth'] + ' ' * (2 * i) + smiley['eyes'])

for i in range(10):
    print(' ' * (i) + smiley['eyes'] + ' ' * (2 * (9 - i)) + smiley['mouth'] + ' ' * (2 * (9 - i)) + smiley['eyes'])


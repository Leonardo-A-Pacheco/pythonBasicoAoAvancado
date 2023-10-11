#verificar conteudo de string

dado = input('entre com o dado a ser analisado ')

analisar = input('entre com o que deseja analisar ')

print(f'buscando {analisar} em {dado}...')


if ( analisar in dado ):
    print(f'{analisar} encontrado!! em {dado} ')
    
else:
    print(f'{analisar} não encontrado!! em {dado} ')
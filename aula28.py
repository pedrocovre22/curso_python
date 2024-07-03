nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print(f'{nome} tem espacos')
    else:
        print(f'{nome} nao tem espacos')

    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios.')

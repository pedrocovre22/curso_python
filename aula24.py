# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 
#  P e d r o
# -6-5-4-3-2
nome = 'pedro'
# print(nome[0])
# print(nome[-2])
# print('ed' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('zero' not in nome)

nome = input('digite seu nome')
encontrar = input('digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')
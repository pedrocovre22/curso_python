pessoa = {}


chave = 'nome'

pessoa[chave] = 'pedro'
pessoa['sobrenome'] = 'covre'
lista= []

print(pessoa[chave])


del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('nao existe')
else:
    print(pessoa['sobrenome'])
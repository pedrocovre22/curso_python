p1 = {
    'nome': 'pedro',
    'sobrenome': 'covre',
}
# print(p1['nome'])
# print(p1.get('nome', 'nao existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# print(p1)
# p1.update(nome='novo valor',idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)
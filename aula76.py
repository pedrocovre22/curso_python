pessoa = {
    'nome': 'Pedro',
    'sobrenome': 'Covre',
    # 'idade': 900,
}

pessoa.setdefault('idade', 12)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.values()))
# print(list(pessoa.keys()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)
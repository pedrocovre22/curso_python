# lista = [4, 32, 4, 2, 342, 3452,312, 4,235, 2]
# lista.sort(reverse=True)

lista = [
    {'nome': 'Pedro', 'sobrenome': 'Covre'},
    {'nome': 'Joao', 'sobrenome': 'Silva'},
    {'nome': 'Daniel', 'sobrenome': 'Pereira'},
    {'nome': 'Charles', 'sobrenome': 'Mendes'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['nome'])


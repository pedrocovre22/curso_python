lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')
lista.append('pedro')

lista_enumerada = list(enumerate(lista))

for indice, nome in lista_enumerada:
    print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('for da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
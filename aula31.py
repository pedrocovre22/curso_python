condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faca algo')
else:
    print('nao faca algo')

if passou_no_if is None:
    print('nao passou no if')
else:
    print('passou no if')

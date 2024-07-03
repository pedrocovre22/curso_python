numero = input('numero digitado sera dobrado: ')

try:
    numero_float = float(numero)
    print('float:', numero_float)
    print(f'o dobro de {numero} é {numero_float * 2:.0f}')
except:
    print('isso nao é um numero')

# if numero.isdigit():
#     numero_float = float(numero)
#     print(f'o dobro de {numero} é {numero_float * 2:.0f}')
# else:
#     print('isso nao é um numero')
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_numero_1 = int(primeiro_valor)
int_numero_2 = int(segundo_valor)

if int_numero_1 > int_numero_2:
    print(f'primeiro_valor={int_numero_1} é maior que o segundo_valor={int_numero_2}')
elif int_numero_1 == int_numero_2:
    print(f'segundo_valor={int_numero_2} é igual o primeiro_valor={int_numero_1}')
else:
    print(f'segundo_valor={int_numero_2} é maior que o primeiro_valor={int_numero_1}')

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input('digite um numero inteiro: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_str = 'impar'

#     if par_impar:
#         par_impar_str = 'par'

#     print(f'o numero {numero_int} é {par_impar_str}')
# else:
#     print('voce nao digitou um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = int(input('que horas sao?'))

# if hora >= 0 and hora <= 11:
#     print('bom dia')
# elif hora >= 12 and hora <= 17:
#     print('boa tarde')
# elif hora >= 18 and hora<= 23:
#     print('boa noite')
# else:
#     print('nao conheco essa hora')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('digite seu nome: ')

if len(nome) <=4:
    print('nome curto')
elif len(nome) <=6:
    print('nome normal')
else:
    print('seu nome é grande')
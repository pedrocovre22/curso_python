"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import re
import sys

entrada = input("Digite um CPF: ") \
.replace('.','')\
.replace(' ','')\
.replace('-','')
digitar_cpf= re.sub(r'[^0-9]','',entrada)
digitos = digitar_cpf[:9]
contador_regressivo = 10
resultado = 0

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('Dados Invalidos')
    sys.exit()

for digito in digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

resultado1 = (resultado * 10) % 11

digitos_2 = digitar_cpf[:10]
contador_regressivo_2 = 11
resultado_1 = 0

for digito_2 in digitos_2:
    resultado_1 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

resultado_2 = (resultado_1 * 10) % 11

cpf_gerado = f'{digitos}{resultado1}{resultado_2}'

if digitar_cpf == cpf_gerado:
    print(f'{digitar_cpf} valido')
else:
    print('CPF invalido')
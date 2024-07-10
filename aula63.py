import random

digitos = ''
for i in range(9):
    digitos += str(random.randint(0, 9))

contador_regressivo = 10
resultado = 0

for digito in digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
resultado1 = (resultado * 10) % 11
resultado1 = resultado1 if resultado1 <= 9 else 0

digitos_2 = digitos + str(resultado1)
contador_regressivo_2 = 11

resultado_1 = 0
for digito_2 in digitos_2:
    resultado_1 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
resultado_2 = (resultado_1 * 10) % 11

cpf_gerado = f'{digitos}{resultado1}{resultado_2}'

print(cpf_gerado)

# senha_salva = '1234'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('aquele laco acima pode ter repeticoes infinitas')
texto = 'python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
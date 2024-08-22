

def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multi(14, 6)
print(multiplicacao)

def par_impar(numero):
    pordois = numero % 2 == 0

    if pordois:
        return f'{numero} é par'
    return f'{numero} é impar'

print(par_impar(2))
print(par_impar(134))
print(par_impar(25))
print(par_impar(7))
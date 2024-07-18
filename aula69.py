x, y, *resto = 1, 2 ,3 ,4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        print('total', total, numero)
        total = total + numero
        print('total', total)


soma(1,2,3,4,5,6)
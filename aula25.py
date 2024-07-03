"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'pedro'
preco = 1000.236666
variavel = '%s, o preco total foi R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %x' % (15, 15))
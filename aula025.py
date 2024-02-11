"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Felipe'
preco = 1000.98424132
variavel = '%s, O preço é: %.2f' % (nome,preco)
print(variavel)
print('O valor em hexadecimal de %d é %08x' % (15, 15))
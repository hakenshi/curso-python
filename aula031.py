"""
Flag (Bandeira) - Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade(ID))
id = identidade
"""

# v1 = 'a'
# v2 = 'a'
# print(id(v1))
# print(id(v2))

condição = True
entrou_no_if = None

if condição	: 
    entrou_no_if = True
    print('Banana')

else : 
    print ('Maçã')

if entrou_no_if is None :
    print('Não entrou no if')

else : 
    print('Entrou no if')
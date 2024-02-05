# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input(f'[E]ntrar [S]air\n')
# input_senha = input('Insira uma senha: \n')
# senha = '123456'
# e
# if (entrada == 'E' or entrada == 'e' and input_senha == senha) :
#     print('Senha correta')
#     print('Entrar')

# else : 
#     print('Senha incorreta.')
#     print('Sair')

# Avaliação de curto circuito:

print(True or True or True or False)
print(True or True or 0 or True)
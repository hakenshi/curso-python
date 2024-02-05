# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  F e l i p e
# -6-5-4-3-2-1 

nome = input('Insira um nome: \n')
letra = input('Insira uma letra a ser buscada no nome: \n')

if letra not in nome: 
    print('Letra inexistente.')
else : 
   print(f'a letra {letra}, não foi encontrada em {nome}.')
   
# if letra in nome: 
#     print(f'a letra {letra}, foi encontrada em {nome}.')

# else : 
#     print(f'a letra {letra}, não foi encontrada em {nome}.')

    
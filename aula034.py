"""
Repetições
While(Enquanto)
executa um código enquanto uma condição for verdadeira
"""

condicao = True

while condicao :
    nome = input('Insira um nome: \n')
    print(f'o nome inserido é: {nome}')
    if nome == 'sair' : 
        break
    
print('Você saiu do programa.')
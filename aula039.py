nome = input('Insira um nome: \n')
nome_length = len(nome)
novo_nome = ''
i = 0

while i < nome_length : 
    letra = nome[i]
    novo_nome += f'*{letra}* '
    i+= 1
novo_nome += ''
print(novo_nome)


"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num1 = input('Insira um número: \n')

# def verifica_par_ou_impar(n) :
#     if n % 2 == 0 :print(f'{n} é um número par')
    
#     else : print(f'{n} é um número ímpar')

# try :
#     n1_float = float(num1)
#     verifica_par_ou_impar(n1_float)

# except : print(f'{num1} não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Insira a hora atual: \n')

# try :
#     hora_do_dia = int(hora)

#     if 0 <= hora_do_dia <= 23 :

#         exibe_bom_dia = hora_do_dia >= 0 and hora_do_dia <= 11

#         exibe_boa_tarde = hora_do_dia >= 12 and hora_do_dia <= 17

#         exibe_boa_noite = hora_do_dia >= 18 and hora_do_dia <= 23

#         if exibe_bom_dia : print(f'O horário atual agora é: {hora_do_dia}h, bom dia!')

#         if exibe_boa_tarde : print(f'O horário atual agora é: {hora_do_dia}h, boa tarde!')

#         if exibe_boa_noite : print(f'O horário atual agora é: {hora_do_dia}h, boa noite!')

#     else : print(f'{hora_do_dia} horário fora do intervalo válido')

# except : print(f'{hora} não é um número inteiro.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input('Insira seu nome: \n')

# tamanho_nome = len(nome)

# if ' ' in nome : print('É só pra colocar o primeiro nome!')

# else :
#     if tamanho_nome <= 4 : print(f'Seu nome tem {tamanho_nome} letras, {nome} é um nome curto.')

#     elif tamanho_nome >= 5 and tamanho_nome <= 6 : print(f'Seu nome tem {tamanho_nome} letras, {nome} é normal.')

#     else : print (f'Seu nome tem {tamanho_nome} letras, {nome} é um nome grande. ')



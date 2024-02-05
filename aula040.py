import emoji
while True:

    n1 = input('Insira um número: \n')
    n2 = input('Insira um número: \n')
    operador = input('Insira um operador [+] [-] [/] [*]: \n')

    numeros_valiods = None

    try :
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_valiods = True
        

    except:
        numeros_valiods = None

    if numeros_valiods is None: 
        print('Algum dos números inseridos é inválido e eu não sei o que fazer com esses números.')
        continue

    operadores_validos = '+-*/'

    if operador not in operadores_validos : 
        print('Insira um operador válido.')
        continue

    if len(operador) > 1 :
        print('Insira somente 1 operador.')
        continue

    if operador == '+' : print(f'{n1} + {n2} = {n1_float+n2_float:.2f}')
    elif operador == '-' : print(f'{n1} - {n2} = {n1_float-n2_float:.2f}')
    elif operador == '*' : print(f'{n1} * {n2} = {n1_float*n2_float:.2f}')
    elif operador == '/' : print(f'{n1} / {n2} = {n1_float/n2_float:.2f}')
    else : print(emoji.emojize('Isso não era para estar aqui:thinking:'))
    

    parar = input('Enecerrar o programa? [S]im :\n').lower().startswith('s')

    if parar : 
        print('Programa encerrado.')
        break

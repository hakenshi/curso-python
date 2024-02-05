n1 = input('Insira um número: \n')
try :
    n1_float = float(n1)
    print(f'O dobro de {n1} é: {n1_float*2}')
    

except:
    print(f'Isso não é um número, eu não sei o que fazer com isso: {n1}')

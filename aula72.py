import random

def multiplicar(*args) :
    resultado = 1

    
    for nums in args:
        resultado *= nums
    
    print ('Números multiplicados:',*args)

    return f'Produto: {resultado}'

array = [random.randint(1,20) for _ in range(0,5)]
    
print(multiplicar(*array))


def isEven(n): return n % 2 == 0

for i in range(1,11):

    if isEven(i): print(f'{i} Par')

    else: print(f'{i} Ímpar')
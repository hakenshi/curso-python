def isEven(num):
    return num % 2 == 0
    


for i in range(1, 21):
    condicaoTenaria = "par" if isEven(i) else "ímpar"
    print(i, condicaoTenaria)


import re
import random

def calcula_digito(cpf,posicao):

    digitos = cpf[:posicao]
    contador_regressivo = 11 if posicao == 10 else 10

    resultado = sum(int(i) *contador_regressivo for i in digitos)
    novo_digito = (resultado * 10) % 11

    return novo_digito if novo_digito <= 9 else 0

def verificaCpf(cpf, novo_cpf): return cpf == novo_cpf

cpf = ''.join(str(random.randint(0,9)) for _ in range(10))

cpf_format = re.sub(r'[^0-9]', '', cpf)

primeiro_digito = calcula_digito(cpf_format,9)
segundo_digito = calcula_digito(cpf_format,10)

novo_cpf = f'{cpf_format[:9]}{primeiro_digito}{segundo_digito}'

if verificaCpf(cpf_format, novo_cpf):
    print(f'{novo_cpf} é um cpf válido')

else:
    print(f'{novo_cpf} não é um cpf válido')

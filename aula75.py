def fatorar(expoente):
   
   def multiplicador(n) : return n ** expoente

   return multiplicador

n = int(input('Insira um número: \n'))

duplicar = fatorar(2)
triplicar = fatorar(3)
quadruplicar = fatorar(4)


print(f'\n{n}² = {duplicar(n)} \n')
print(f'{n}³ = {triplicar(n)} \n')
print(f'{n}⁴ = {quadruplicar(n)} \n')
frase = 'Banana Maçã Pêssego'

i = 0
maior_contagem = 0
letra_mais_frequente = ''
while i < len(frase):
    letra_atual = frase[i]
    contagem_letra = frase.count(letra_atual)
    if contagem_letra > maior_contagem:
        maior_contagem = contagem_letra
        letra_mais_frequente = letra_atual
    i += 1

print(f'A letra que mais aparece é: {letra_mais_frequente}, ela aparece {maior_contagem} vezes')

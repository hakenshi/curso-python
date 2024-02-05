import emoji
string = 'Limão'

i = 0

while i < len(string) :
    letra = string[i]

    if letra == ' ' : break
    
    print(letra)
    i+=1

else :
    print(emoji.emojize('não encontrei um espaço na string :thinking_face:'))

print('Esse print foi inserido fora do laço while')
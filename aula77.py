import random
import os
perguntas = [
    {
        'pergunta': 'Qual a resposta para a vida, a verdade e o universo?',
        'opcoes': ['42', '78', '34', '24'],
        'resposta': '42'
    },

    {
        'pergunta': 'Qual o valor de PI?',
        'opcoes': ['3.14', '2.71', '1.618', '4.20'],
        'resposta': '3.14'
    },

    {
        'pergunta': 'Qual o maior planeta do Sistema Solar?',
        'opcoes': ['Terra', 'Júpiter', 'Marte', 'Vênus'],
        'resposta': 'Júpiter'
    },

    {
        'pergunta': 'Brittle Bones Nicky Was?',
        'opcoes': ['Crafty And Tricky', 'Bicthy and Nifty', 'That Son Of A Bitch Was Gold', 'A kid'],
        'resposta': 'Crafty And Tricky'
    }

]

tentativas = 3
chave_aleatoria = random.randint(0, len(perguntas)-1)

while (tentativas > 0):
    print(f'Contagem de tentativas: {tentativas}\n')

    pergunta = perguntas[chave_aleatoria]['pergunta'], '\n'

    opcoes = perguntas[chave_aleatoria]['opcoes']

    resposta_key = perguntas[chave_aleatoria]['resposta']

    print(*pergunta)

    for i, opcoes in enumerate(opcoes, 1):
        print(f'{i}. {opcoes}')

    resposta = input('Insira uma resposta: \n')

    
    if resposta.lower() == resposta_key.lower() :
        os.system('clear')
        print(f'Resposta: {resposta_key}') 
        print('\nVocê acertou!\n')
        break

    elif resposta not in opcoes:
        os.system('clear')
        print('\nResposta incorreta inserida.\n')
        tentativas -= 1

    if tentativas <= 0:
        os.system('clear')
        print('Suas tentativas chegaram a zero.')
        print(f'a resposta correta era: {resposta_key}')
        print('programa encerrado.')
        break

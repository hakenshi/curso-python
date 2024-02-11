import random
import os
PERGUNTAS = [
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

TENTATIVAS = 3
CHAVE_ALEATORIA = random.randint(0, len(PERGUNTAS)-1)

while (TENTATIVAS > 0):
    print(f'Contagem de tentativas: {TENTATIVAS}\n')

    pergunta = PERGUNTAS[CHAVE_ALEATORIA]['pergunta'], '\n'

    opcoes = PERGUNTAS[CHAVE_ALEATORIA]['opcoes']

    resposta_correta = PERGUNTAS[CHAVE_ALEATORIA]['resposta']

    print(*pergunta)

    for i, opcoes in enumerate(opcoes, 1):
        print(f'{i}. {opcoes}')

    resposta_usuario = input('Insira uma resposta: \n')

    
    if resposta_usuario.lower() == resposta_correta.lower() :
        os.system('clear')
        print(f'Resposta: {resposta_correta}') 
        print('\nVocê acertou!\n')
        break

    elif resposta_usuario not in opcoes:
        os.system('clear')
        print('\nResposta incorreta inserida.\n')
        TENTATIVAS -= 1

    if TENTATIVAS <= 0:
        os.system('clear')
        print('Suas tentativas chegaram a zero.')
        print(f'a resposta correta era: {resposta_correta}')
        print('programa encerrado.')
        break
'''3. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto ou de um vetor e será escolhida uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.'''

import random

palavras = ["banana","cachorro","tinta","porta","paris","Cachorro","montanha","violão","sorriso","amizade","lua","felicidade","chave","aventura","chocolate","oceano","arco-íris","vela","floresta"]
palavra_aleatoria = random.choice(palavras)
palavra_list = list(palavra_aleatoria)
random.shuffle(palavra_list)
palavra_embaralhada = ''.join(palavra_list)

numero_tentativas = 1

print(f'Você tem 6 tentativas para acertar a seguinte palavra:')
print("----------------")
print(palavra_embaralhada)
print("----------------")

while numero_tentativas <= 6:
    tentativa = input(f'Tentativa numero {numero_tentativas}: ')
    tentativa.lower()
    if tentativa.lower() == palavra_aleatoria:
        print(f'Você adivinhou em {numero_tentativas} tentativas!! a palavra realmente era {palavra_aleatoria.capitalize()}')
        break
    else:
        numero_tentativas += 1
        if numero_tentativas == 7:
            print(f'Você usou todas as chances, a palavra era {palavra_aleatoria}')

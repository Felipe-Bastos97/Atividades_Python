import random
from random import randint

print('Sou seu computador ...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ?')
print('Qual o seu palpite ? ')
numero=int(input())
aleatorio=random.randint(1,10)
acertou= False
palpite=0

while not acertou :

    if numero == aleatorio:
         print('Acertou o numero que eu pensei ')
         acertou = True
         palpite += 1

    elif aleatorio > 5:
        print('Maior que 5')
        numero = int(input('Errou tente denovo'))
        palpite+=1
    elif aleatorio < 5:

        print('Menor que 5')
        numero = int(input('Errou tente denovo'))
        palpite += 1

print('Fim o numero que eu pensei {}'.format(aleatorio))
print('Acertou com {} palpites'.format(palpite))
from random import randint
from time import sleep

computador=randint(0,5)#faz o sorteio de 0 a 5

print('-=-'*20)
print('Vou pensar em um numero de 0 a 5 tente adivinhar!!')
print('-=-'*20)

n=int(input('Digite um valor de! '))
print('Processando...')
sleep(2)#Faz uma pausa de 2 segundos para continuar
if n==computador:

    print('Você acertou meu numero é {}'.format(computador))
else:
    print('Errei o seu numero eu pensei no numero {} e não no numero {}'.format(computador,n))
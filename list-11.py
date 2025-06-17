import random

logo='Mega Sena'
num=0
lista=list()
cont=0
print('-='*30)
print(f'{logo:^60}')
print('-='*30)
resp=int(input('Digite quantas vezes quer fazer o jogo: '))
for i in range(0,resp):
    for l in range(0, 6):

            num = random.randint(1, 60)
            lista.append(num)

    lista.sort()
    print(f'{lista} ',end='')  #:^5 centraliza em 5 caractere
    print()
    lista.clear()


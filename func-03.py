import time

def cont(ini,fi,sa):
    if ini > fi:
        sa*=-1
    if sa == 0 :
        sa=1
    print('Contagem de 1 ate 10 de 1 em 1 = ', end='')
    for i in range(1,11):
        print(f'{i}',end=' ')
        #time.sleep(0.5)
    print()
    print('Contagem de 10 ate 1 de 2 em 2 = ', end='')
    for i in range(10, 0, -2):
        print(f'{i}', end=' ')
        #time.sleep(0.5)
    print()


    for i in range(ini,fi,sa):
        print(f'{i}',end=' ')


print('Testando for')
inicio=int(input('Digite o inicio da contagem'))
final=int(input('Digite o final da contagem'))
salto=int(input('Digite o salto da contagem'))
cont(inicio,final,salto)
from random import randint


numeros=list()
sor=list()

def sorteia(lista):
    print('Sorteando 5 Valores da lista')
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n)
        print(f'{n}',end=' ')


def somapar(lista):
    soma=0
    for valor in lista:
        if valor % 2==0:
            soma+= valor
    print(f'Somando os pares de {lista} temos {soma}')

sorteia(numeros)
somapar(numeros)

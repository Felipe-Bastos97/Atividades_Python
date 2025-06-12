

menor=0
maior=0


for i in range(1,6):
    n=float(input('Digite o {} peso da pessoa:'.format(i)))
    if i==1:
        maior = n
        menor = n
    else:
        if n > maior :
            maior = n

        if n < menor:
            menor = n


print('O numero maior é {}'.format(maior))
print('O numero menor é {}'.format(menor))
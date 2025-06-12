
print('Gerador de PA')

n1=int(input('Primeiro termo'))
n2=int(input('Razão da PA'))
termo=n1
cont=1
while cont <=10:
    print('{} >'.format(termo),end=' ')

    termo=termo+n2
    cont+=1

print('O n1  esta com o valor {}\n'.format(n1))
print('O termo esta com o valor {}\n'.format(termo))

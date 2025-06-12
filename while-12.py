
print('Gerador de PA')

n1=int(input('Primeiro termo'))
n2=int(input('Razão da PA'))
termo=n1
cont=1
total=0
mais=10
while mais !=0:
    total=total+mais
    while cont <=total:
        print('{} >'.format(termo),end=' ')

        termo=termo+n2
        cont+=1
    print('Pausa')
    mais=int(input('Quantos Termos você quer a mais? '))
print('Progressao finalizada com {} termos mostral'.format((total)))

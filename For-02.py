
soma=0
cont=0
for i in range(1,7):

    n=int(input('Digite o {} Valor'.format(i)))
    if n % 2==0:
        soma= n + soma
        cont +=1
print(soma,cont)

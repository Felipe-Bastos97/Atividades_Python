print('Sequência de Fibonacci')
n=int(input('Digite quantos termos você quer mostrar ?'))
cont=2
fib=0
n2=1
print('{} > {} > '.format(fib,n2),end='')

while cont != n:
    n3 = fib + n2
    print('{} >'.format(n3),end=' ')
    fib= n2
    n2=n3



    cont += 1
print('Fim')

num=(int(input(f'Digite 1 Valor')),
int(input(f'Digite 2 Valor')),
int(input(f'Digite 3 Valor' )),
int(input(f'Digite 4 Valor')))

print(f'{num}')
print(f'o valor 9 apareceu quantas vezes {num.count(9)} vezes ')
print(f'O valor 3 apareceu {num.index(3)}')#mostra o posição do objeto ('.index()')
for n in num:
    if n%2==0:
        print(f'{n} ,',end=' ')

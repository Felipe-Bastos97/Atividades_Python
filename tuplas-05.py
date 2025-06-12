listagem=('Lápis',1.75,
          'Borracha',2,
          'Caderno',15.90,
          'Estojo',25,
          'Mochila',120.20)
l='-'*40
print(l)
print(f'{"Listagem de preços escolar":^35}')#Espassamento de caractere ^
print(l)
for pos in range(0,len(listagem)):
    if pos % 2==0:# lapis par preço impar /produto a direira e preço a esquerda

        print(f'{listagem[pos]:.<30}',end='')# sequencia de pontos alinhados, 30 seria quantidade caractere total
    else:
        print(f'R$ {listagem[pos]:.2f}')
print(l)
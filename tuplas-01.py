#tuplas são imutáveis nao pode mexer em execução

lanche=('Hamburguer','Suco','Pizza', 'Pudim','Batata-Frita')
print(sorted(lanche))#coloca em ordem

for c in lanche:
    print(f'{c}',end=' ')

for cont in range(0,len(lanche)):
    print(f'{lanche[cont]} na posição {cont}')

for pos, c in enumerate (lanche):
    print(f'{c} na posição {pos}',)


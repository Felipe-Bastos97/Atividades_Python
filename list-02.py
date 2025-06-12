

'''
a=[2,5,8]
b=a (Estou fazendo uma ligação com a e b
b=a[:] (Estou fazendo uma copia de dados )
'''
num=list()
for cont in range(0,5):
    num.append(int(input('Digite um Valor')))


for c,n in enumerate(num):#Quando precisa tanto do índice quanto do valor em loops.
    print(f'Na posição {c} encontrei o valor {n}')
print('Cheguei ao final da Lista')

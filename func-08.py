
def fatorial(x,show=False):
    '''
    -> Calcula Fatorial de um número
    :param x:Recebe o valor e multiplica pelo antecessor:
    :return: e retorna o soma do valor
    '''
    f=1
    for i in range(x,0,-1):#Fatorial
        if show==True:
            print(f'{i} x',end=' ')
        f*=i
    return f

res=int(input('Digite um valor'))
fatorial(res)
print(f'o fatorial de {res} e : {fatorial(res,show=True)}')

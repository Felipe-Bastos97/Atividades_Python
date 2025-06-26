#help() da uma discrição do comando ou manual
help(print)
def contador (i=0,f=0,p=0):#São parâmetros opcionais caso nao seja informado o valor
    """"
    :para i: inicio da contagem
    :para f: fim da contagem
    :para p: passo da contagem
    :return sem retorno
    """
    #docString -------------------
    c=i
    while c <= f:
       print(f'{c}',end=' ')
       c+=p
    print('Fim')

contador(3,20,1)

def somar(a,b,c):
    s=a+b+c
    #print(f'A soma vale {s}')
    return s

print(somar(1,2,5))

resp=somar(1,5,8)
print(resp)

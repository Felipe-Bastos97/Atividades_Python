def escreva(al):
    x=len(al)+4#contar quantos caracteres tem e contar
    print('-' * x)
    print(f'  {al}')
    print('-' * x)


al=str(input('Escreva algo: '))
escreva(al)

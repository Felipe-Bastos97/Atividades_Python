

numero1=int(input('Digite o primeiro valor'))
numero2=int(input('Digite o Segundo valor'))
total=0
x=0

while x != 5:
    print('[1] SOMAR \n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGRAM\n')
    print('Selecione uma das opções')

    x = int(input())

    if x == 1:
        total = numero1 + numero2
        print('O valor que deu é {}'.format(total))

    elif x == 2:
        total = numero1 * numero2
        print('O valor que deu é {}'.format(total))

    elif x==3:
        if numero1>numero2:
            total = numero1
            print('O valor que deu é {}'.format(total))
        else:
            total=numero2
            print('O valor que deu é {}'.format(total))

    elif x==4:
        numero1 = int(input('Digite o primeiro valor'))
        numero2 = int(input('Digite o Segundo valor'))

    elif x ==5:
       print ('Fim')



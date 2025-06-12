print('--------------Lojas Guanabara-----------')
valor=int(input('Digite o valor da compras\n'))


print('[1] à vista dinheiro:')
print('[2] à vista no cartão: ')
print('[3] em até 2x no cartão:')
print('[4] 3x ou mais no cartão:')

pg=int(input('Digite qual forma de pagamento\n'))

if pg == 1:
    print('O valor da suas compras e de {} com desconto ficara {}'.format(valor,valor-((10/100)*valor)))

elif pg== 2:
    print('O valor da suas compras e de {} com desconto ficara {}'.format(valor, valor - ((5 / 100) * valor)))


elif pg==3:
    print('O valor da suas compras e de {} parceldado em 2X'.format(valor))


elif pg ==4:
    pa=int(input('Em quantas vezes você quer parcelar ?'))

    print('O valor da suas compras parcelado em {}x ou mais e de {} '.format(pa,valor+((20 / 100) * valor)))

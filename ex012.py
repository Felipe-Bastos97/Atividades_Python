num=int(input('Digite um valor'))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
md=num//10000%10


print('Analisando o numero {}'.format(num))
print('Unidade -{}'.format(u))
print('Dezena -{}'.format(d))
print('Centena -{}'.format(c))
print('Milhar -{}'.format(m))
print('Milhar/2 -{}'.format(md))

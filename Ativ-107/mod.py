from uteis import moeda


p= float(input('Digite o preço : R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% {p} é {moeda.aumentar(p,10)}')
print(f'Diminuindo em 10% {p} é {moeda.diminuir(p,10)}')


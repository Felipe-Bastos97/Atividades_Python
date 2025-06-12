num=list()

cxm=cx=menor=maior=0
for i in range(0,5):
    num.append(int(input(f'Digite um valor para a posicão {i}:')))
    if i == 0:
        maior = menor = num[i]

    if num[i] < menor:
        menor = num[i]
        cx=i

    if num[i] > maior:
        maior = num[i]
        cxm=i



for c,i in enumerate(num):
    print(f' A posição {c} esta o numero {i}')


print(f'O Menor numero é {menor} esta na posição {cx}')
print(f'O Maior numero é {maior} esta na posição {cxm}')

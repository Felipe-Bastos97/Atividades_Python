
def val(*num):#Colocar o * ele vai aceitando todos os paramentros que forem informados no codigo principal
    cont=maior=0
    print('-'*40)
    print('\nAnalisando os valores passados...')#quebra de linha \n

    for i in num:
        print(f'{i} ',end='')
        if i == 0:
            maior=i
        else:
            if i > maior:
                maior=i
            cont+=1

    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor é {maior}')






val(2,9,4,5,7,1)
val(4,7,0)
val(6)
val()
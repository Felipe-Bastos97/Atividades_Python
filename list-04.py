numeros=list()

while True:
    n=int(input('Digite um valor:'))

    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com Sucesso')
    else:
        print('Valor Duplicado')

    r=str(input('Deseja continuar?[S/N]'))
    if r in 'Nn':
        break
print(f'Você digitou os valores {numeros}')

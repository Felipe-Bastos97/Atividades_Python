
total=cont=0
contpreco=0
maiorp=0
menorp=0
produto=' '
while True:


    produto=str(input('Digite o nome do produto'))
    preco=float(input('Preço do produto'))
    continuar=str(input('Deseja adicionar mais um produto S/N: ')).strip().upper()[0]
    total = preco + total
    cont += 1
    if cont ==1 or preco < menorp:
        menorp=preco
        produto2 = produto

    if preco >= 1000:
       contpreco += 1



    if continuar == 'N':
        break

print(f'O valor das compras é , R${total}')
print(f'Tem {contpreco} , produtos acima de R$1000')
print(f'O produto com menor preço é {menorp} e produto e {produto2}')




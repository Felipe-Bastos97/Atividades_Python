valores = []
while True :
    valores.append(int(input('Digite um Valor')))
    res=str(input('Quer continuar: [S/N]'))
    if res in 'Nn':
        break
print('-'*30)
print(f'{len(valores)}')
valores.sort(reverse=True)#ordem decrescente
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O 5 faz parte dessa lista')
else:
    print('O 5 não faz parte dessa lista')
from django.template.defaultfilters import upper

galera=list()
pessoa=dict()
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome : '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo : [M/F]')).upper()[0]#primeira Letra

        if pessoa['sexo'] in 'FM':
            break
        else:
            print('Informe [F/M] para sexo')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())#Cria uma Copia

    while True:
        resp=str(input('Quer continuar S/N? ')).upper()[0]
        if resp in 'SN':
            break
        print('Informe [S/N]!')
    if resp == 'N':
        break

media=soma/len(galera)
print(f'Temos o valor {len(galera)} cadastrado')
print(f'A media das idades {media}')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'As mulheres cadastrada foram {p['nome']}')
print()
print('-='*30)
for p in galera:
    if p['idade'] >= media:
        for k,v in p.items():
            print(f'{k} = {v}')
print()
print('<<<<Encerrando>>>>')
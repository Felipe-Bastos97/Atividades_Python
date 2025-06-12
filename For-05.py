

contM=0
contM2=0
somaidade=0
mediaidade=0
homeV=''

for i in range(1,5):
    print('----------------{} Pessoa -------------'.format(i))
    nome = str(input('Digite o {} nome:'.format(i)))
    idade = int(input('Digite o {} idade:'.format(i)))
    sexo = str(input('Sexo: [M/F]:'))
    somaidade+= idade

    if i == 1 and sexo in 'Mm':# in 'Mn' pega as 2 caractere
        homeV=nome
        maioridade=idade
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        homeV=nome
    if sexo in 'Ff' and idade <20:
        contM+=1





mediaidade= somaidade/4
print('A {} média das idades e '.format(mediaidade))
print('O homen, mais velho é {} '.format(homeV))
print('Ao todo da mulheres com menos e 20 anos e {}'.format(contM))

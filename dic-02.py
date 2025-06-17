pessoas={'nome':'','media':0}
pessoas["nome"]=str(input('Digite o nome: '))
pessoas["media"]=float(input('Digite a média: '))
print(f'Nome é igual a {pessoas["nome"]}')
print(f'Média é igual a {pessoas["media"]}')

if pessoas["media"] <= 7 :
    print('Situação é igual a reprovado')
else:
    print('Situação é igual a aprovado')
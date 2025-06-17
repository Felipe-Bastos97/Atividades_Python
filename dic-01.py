pessoas={'nome':'Gustavo','Sexo':'M', 'idade':22}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
pessoas['Peso']= 98.5 #Adicionar dentro do dicionario

print('-='*30)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('-='*30)
for k in pessoas.keys():#
    print(k)

print('-='*30)
for k,c in pessoas.items():#
    print(f'{k} = {c}')

print('-='*30)
brasil=list()
estado1={'uf':'Rio de Janeiro','Sigla':'RJ'}
estado2={'uf':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
from datetime import datetime

pessoas={'nome':'','ano':0,'ct':0 ,'salario':0,'anoct':0}

pessoas["nome"]=str(input('Nome :'))
nasc=int(input('Ano de nascimento :'))
pessoas["ct"]=int(input('Carteira de Trabalho ( 0 não tem):'))

pessoas["ano"]=datetime.now().year-nasc



if pessoas["ct"]==0:
    print('-='*40)
    print(f'Nome tem o valor {pessoas["nome"]}')
    print(f'Idade tem o valor {pessoas["ano"]}')
    print(f'CTPS tem o valor {pessoas["ct"]}')
else:
    pessoas["salario"] = int(input('Salário : R$'))
    pessoas["anoct"] = int(input('Ano de contratação :'))
    aposent=pessoas['ano']+((pessoas["anoct"]+35)-datetime.now().year)
    print()
    print(f'Nome tem o valor {pessoas["nome"]}')
    print(f'A idade tem o valor {pessoas["ano"]}')
    print(f'CTPS tem o valor {pessoas["ct"]}')
    print(f'Ano de Contratação é {pessoas["anoct"]}')
    print(f'Salário tem o valor de  R${pessoas["salario"]}')
    print(f'Aposentadoria vai ser daqui {aposent}')


print('-='*40)

temp=list()
princ=list()
resp=''
mai=men=0
while True:
    temp.append(str(input('Digite o nome:')))#Posiçao 0 na lista
    temp.append(float(input('Digite o peso:')))#Posição 1 na lista
    if len(princ) == 0:# se for o primeiro dado ele vai add o dados no maior e no menor
        mai=men=temp[1]
    else:
        if temp[1]> mai:
            mai=temp[1]

        if temp[1] < men:
            men=temp[1]

    princ.append(temp[:])# Cria uma copia [:] dos dados
    temp.clear()#Limpar o temp para nao duplicar no print
    resp=str(input('Deseja continuar ? [S/N]').upper())
    if resp == 'N':
        break

print('-='*30)
print(f'Os Dados foram {princ}')
print(f'Ao todo foram cadastrados {len(princ)}')#Vai contar quantos compartimentos tem

print(f'As pessoas com mais pessadas são ',end='')
for p in princ:
    if p[1]==mai:
        print(f'[{p[0].upper()}] com {p[1]} kg')

print(f'As pessoas com menos pesos são',end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0].upper()}] com {p[1]} kg')




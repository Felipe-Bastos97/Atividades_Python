
valores=[]
listapar=[]
listaimp=[]

while True :
    valores.append(int(input('Digitar Valores :')))
    if 0 in valores :
      break

for i,c in enumerate (valores):
     if valores[i]==0:
         break
     elif valores[i] % 2 == 0:
        listapar.append(c)
     else:
        listaimp.append(c)
print(f'Numeros pares são {listapar}')
print(f'Numeros impares são {listaimp}')




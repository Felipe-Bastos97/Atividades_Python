num=[[],[]]#colchetes posição 0 e o outro posição 1
valor=0
for i in range (1,8):
    valor=int(input(f'Digite o {i} valor'))

    if valor % 2 ==0:
        num[0].append(valor)#vai adicionar na posiçao 0 os pares
    else:
        num[1].append(valor)# vai adicionar os impares na posição 1
        
num[0].sort()#organizar em ordem crescente pares
num[1].sort()#organizar em ordem crescente impares

print(f'Todos os valores pares são {num[0]} ')
print(f'Todos os valores impares são{num[1]} ')

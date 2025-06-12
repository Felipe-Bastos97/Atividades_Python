import random

n=int(input('Digite o quantos numeros aleatorios você quer'))

for i in range(n):
   nome=['Pedro','Lucas','joao','marcos','tafarel']
   r=random.sample(nome,1)
   print(r)



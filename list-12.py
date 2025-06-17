import fake
from faker import Faker
import random

fake=Faker('pt_BR')
ficha= list()
for i in range(0,3):
    nome=str(input('Digite o nome :')) or fake.first_name()#Coloca nomes aleatorios se deixar em branco o input
    nota1=float(input('Digite a nota 1: '))
    nota2=float(input('Digite a nota 2: '))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])

print('-='*30)
print(f'{'No':<4} {'Nome':>10}{'Média':>25}')
print('-'*60)
for i,a in enumerate(ficha):
    print(f'{i} {a[0]:>15} {a[2]:>20}')
    print('-'*60)
while True:
    print('-'*60)
    opc=int(input('Mostrar qual aluno digite o No :'))
    if opc <= len(ficha)-1:
        print(f'Notas de ficha {ficha[opc][0]} são {ficha[opc][1]}')


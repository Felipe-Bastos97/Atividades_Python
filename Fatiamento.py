n='   Curso em vídeo ,hello guys estamos here '
print('001',n.find('os'))#Em que momento começou a string os
print('01',n.count('m'))#vai contar quantas vezes aparece o 'm'
print('02',len(n))#Vai contar quantos caracteres tem na string
print('03','Curso' in n)#vai conferir se tem a palavra curso na string e retornar bool
print('-'*20)# multiplica a string
print(n)
print('-'*20)

print('1',n[10:18])#da posição 10 a 18

print('2',n.replace('hello','Android'))#Subistitui as palavras
semesp=n.replace(' ','')# remove todos os espaços da string
print('2.5 ',len(semesp))

print('3',n.upper())# Coloca todas maiúsculas
print('4',n.lower())#Coloca Todas em mainúsculas
print('5',n.capitalize())#Pega string toda e coloca so a Primeira em maiúscula
print('6',n.title())#Aonde tiver quebra de espaço e coloca a primeira maiúsculas
print('7',n.strip())#Remove caracteres vazios no inicio e no fim
print('8',n.rstrip())#remove so os ultimos espaços da direita
print('9',n.lstrip())#remove so o primeiro espaço da esquerda

print('10',n.split())#Dividi uma string em uma lista tirando os espaços vazios
dividido=n.split()
dividido2=n.split()
print(dividido[0],dividido[-1])#primeiro e ultimo nome

print('11','-'.join(n))#vai juntar todas as strings e colocar o - nas divisões


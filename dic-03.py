from random import randint
from operator import itemgetter
jogo={'jogador 1':randint(1,6),
'jogador 2':randint(1,6),
'jogador 3':randint(1,6),
'jogador 4':randint(1,6)  }
rank=list()
print('Valores sorteados')
for l,c in jogo.items():
    print(f'{l} tirou {c} no dado')
rank=sorted(jogo.items(), key=itemgetter(1), reverse=True)#Comando para organizar dicionario
print('-='*30)

for i,v in enumerate(rank):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')#i+1 e para contagem começar do 1 e nao do 0
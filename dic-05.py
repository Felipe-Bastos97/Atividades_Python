jogador=dict()
partida=list()
jogador['nome']= str(input('Nome do Jogador'))
tot=int(input(f'Quantas Partidas {jogador["nome"]} jogou?'))
print('-='*30)

for c in range(0,tot):
    partida.append(int(input(f'Quantos gols na partida {c+1}?')))
jogador['gols']=partida[:]
jogador['total']=sum(partida)#somar
print(jogador)

print('-='*30)
for c,i in jogador.items():
    print(f'O campo {c} tem o valor {i}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])}')
print('-='*30)
for c, i in enumerate(jogador["gols"]):
    print(f'Na partida {c+1}, fez {i} gols')

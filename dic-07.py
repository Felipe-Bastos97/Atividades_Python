time=list()
jogador=dict()
partida=list()

while True:
    jogador.clear()
    jogador['nome']= str(input('Nome do Jogador'))
    tot=int(input(f'Quantas Partidas {jogador["nome"]} jogou?'))
    partida.clear()
    print('-='*30)
    for c in range(0,tot):
        partida.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador['gols']=partida[:]
    jogador['total']=sum(partida)#somar
    time.append(jogador.copy())
    while True:
        resp=str(input('Quer continuar [S/N]?')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*40)
for i in jogador.keys():
    print(f'cod {i:<15}', end='')
print()
print('-='*40)
for i,j in enumerate(time):
    print(f'{i:>3} ',end='')
    for k in j.values():
        print(f'{str(k):<15}',end='')
    print()
print('-='*40)
while True:
    busca=int(input('Mostrar dados de qual jogador:(999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print('Não exite jogador informado.')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}')
        for i,g in enumerate(time[busca]['gols']):
            print(f'No jogo {i} fez {g} gols')
    print('-='*40)

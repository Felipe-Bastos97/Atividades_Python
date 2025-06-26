def ficha(jog='<desconhecido>',gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n=str(input('Digite um Nome:'))
g=str(input('Numero de Gols:'))
if g.isnumeric():#Se g contém apenas números (ex: "5"), ele é convertido para int
    g=int(g)
else:#se nao ele vira 0
    g=0
if n.strip()=='':#n.strip() remove espaços em branco. Se ficar vazio, significa que o nome não foi digitado.
    ficha(gol=g)
else:
    ficha(n,g)

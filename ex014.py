nome=str(input('Digite seu Nome ')).upper().strip()# deixar ja em letras maiúsculas e tirar os espaços da direita e esquerda


print('Quantas vezes a Letra A aparece ! {}'.format(nome.count('A')))
print('Em qual posição ela aparece a primeira vez! {}'.format(nome.find('A')+1))
print('Em qual posição ela aparece a ultima vez! {}'.format(nome.rfind('A')+1))


nc=str(input('Digite seu Nome 2 ')).upper().strip()# deixar ja em letras maiúsculas e tirar os espaços da direita e esquerda
dividido=nc.split()


print('Seu primeiro nome é ! {}'.format(dividido[0]))
print('Seu ultimo nome é! {}'.format(dividido[len(dividido)-1]))#Posso colocar o len dentro da seleção


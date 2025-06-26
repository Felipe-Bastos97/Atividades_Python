
def ajuda(com):
    help(com)
def titulo(msg):
    tam=len(msg)+2
    print('~'*tam)
    print(f' {msg}')
    print('~'*tam)




comando=''
while True:
    titulo('Sistema de ajuda PyHelp')
    comando=str(input('Função ou Biblioteca : '))
    if comando.upper()== 'FIM':
        break
    else:
        ajuda(comando)
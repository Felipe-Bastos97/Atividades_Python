#tuplas são imutáveis nao pode mexer em execução

numero=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    n=int(input('Digite um valor '))
    if 0 < n >= 20:
        print('Tente novamente:\n',end=' ')
    if 0 > n <= 20:
        print(f'Você digitou o numero {numero[n]}')
    x=str(input(('Você quer digitar mais 1 numero S/N ?')).strip().upper())
    if x == 'N':
        break

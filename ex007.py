n=float(input('Qual salario do funcionário ? R$'))
print('Um funcionario que ganhava R${}, com 15% de aumento , passa a receber R${:.2f}'.format(n,(n*15/100)+n,))
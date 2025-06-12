sexo= str(input('Digite M/F')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo=str(input('Dados inválidos.Por favor, Informe seu sexo:')).upper()
print('Sexo {} registrado com sucesso'.format(sexo))
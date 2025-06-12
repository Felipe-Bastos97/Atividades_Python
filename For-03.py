

primeiro=int(input('Digite o primeiro termo :'))
razão=int(input('Razão :'))
decimo=primeiro +(10-1)*razão
for i in range(primeiro,decimo,razão):
    print(i,end=' ')
print('Acabou')

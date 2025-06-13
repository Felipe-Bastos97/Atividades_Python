
import random
totp=c3=mai=0
num = [[0,0,0], [0,0,0], [0,0,0]]  # colchetes posição 0 e o outro posição 1 e ultima 2

for l in range(0,3):#ele vai andar na linha
    for c in range(0,3):# esse vai andar nas colunas
        num[l][c]=random.randint(1,10)
        print(f'[{num[l][c]:^5}] ',end='')#:^5 centraliza em 5 caractere

        if num[l][c] % 2 ==0:
            totp += num[l][c]
        if num[l][2]:# se for a coluna 2 ele vai somar
            c3 +=num[l][2]


        if num[1][c]:
            if num[1][c]>mai:
                mai=num[1][c]

       
    print()

print(f'A soma do valores pares é {totp}')
print(f'A soma da coluna 3 : {c3}')
print(f'O maior valor da linha 2 é : {mai}')




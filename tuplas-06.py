palavra=('Aprender','Programar','Linguagem','Python','Curso','Gratis','Estudar','Praticar','Trabalhar','Mercado')
for p in palavra:
    print (f'\nNa palavra {p} temos',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print (letra,end='')

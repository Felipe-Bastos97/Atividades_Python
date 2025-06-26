from datetime import datetime

from django.db.models.expressions import result


def voto(nascimento):
    # Pode importar bibliotecas dentro de funções economiza memoria
    global result

    datatual=datetime.now().year
    result=datatual-nascimento
    if 16 <= result <=59:# Nesse modelo verefica se esta entre 18 e 59
        return'Voto Obrigatório'
    elif result>=60:
        return 'Voto opcional'
    else:
        return 'Voto negado menor de idade'



ano=int(input('Data de nascimento'))
voto(ano)
print(f'Você tem {result} anos:{voto(ano)}')

def notas(*num,sit=False):
    '''
    -> função para analisar situações de varios alunos.
    :param num: uma ou mais notas dos alunos (aceira varias)
    :param sit:valor opcional indicando se deve ou nao adicionar a situação
    :return:dicionario com várias informaçoes sobre a situação da turma
    '''
    r=dict()
    r['total']=len(num)
    r['Maior']=max(num)
    r['Menor']=min(num)
    r['Média']=sum(num)/len(num)
    if sit:
        if r['Média']>=7:
            r['Situação']='Situação Boa'

        elif r['Média']>=5:
            r['Situação']='Situação Razoavel'

        else:
            r['Situação']='Situação Ruim'
    return r


resp=notas(5.5,8.5,10.6,5,sit=True)
print(resp)
help(notas)


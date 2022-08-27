def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunas (aceita várias).
    :param sit: valor opcional se deve ou não indicar a situação.
    :return: dicionário com várias informações com a situação da turma.
    """
    nota = {}
    nota['total'] = len(num)
    nota['maior'] = max(num)
    nota['menor'] = min(num)
    nota['media'] = sum(num) / len(num)
    if sit:
        if nota['media'] >= 7:
            nota['situação'] = 'BOA'
        if 6 <= nota['media'] < 7:
            nota['situação'] = 'RAZOÁVEL'
        if nota['media'] < 6:
            nota['situação'] = 'RUIM'
    return nota


resp = notas(5.5, 6.5, 5, 7, sit=True)
print(resp)
help(notas)

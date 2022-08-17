lista = list()
aluno = list()
notas = list()
while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    lista.append(aluno[:])
    aluno.clear()
    notas.clear()
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        print(f'No. {"NOME":^25} {"MÉDIA":>}')
        for c1, v1 in enumerate(lista):
            print(f'{c1} {v1[0]:^30}{sum(v1[1])/2:>.1f}')
        break
while True:
    n1 = int(input('Mostrar as notas de qual aluno(No.)? [999 para parar]: '))
    if n1 == 999:
        break
    for c, v in enumerate(lista):
        if n1 == c:
            print(f'As notas de {v[0]} foram {v[1]}')
from time import sleep
print('FINALIZANDO')
sleep(1)
print('VOLTE SEMPRE')




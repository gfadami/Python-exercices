lista = []
grupo = {}
idadeTot = 0
while True:
    grupo['nome'] = str(input('Nome: '))
    while True:
        grupo['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if grupo['sexo'] in 'MF':
            break
        print('ERRO. Por favor digite M ou F:')
    idade = input('Idade: ')
    while not idade.isdigit():
        idade = input('Digite um número válido.\nIdade: ')
    idade = int(idade)
    grupo['idade'] = idade
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Por favor digite S ou N.')
    lista.append(grupo.copy())
    idadeTot += grupo['idade']
    if resp == 'N':
        break
media = idadeTot / len(lista)

print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é {media:.2f}.')
print(f'- As mulheres do grupo são ', end=' ')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print(f'- Lista de pessoas acima da média:')
for p in lista:
    if p['idade'] >= media:
        for k,v in p.items():
            print(f'{k} = {v}.', end='')
            print()
print('FIM')








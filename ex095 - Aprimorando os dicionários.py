jogador = {}
time = []
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    partidas.clear()
    for p in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {p+1}?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N.')
    if resp == 'N':
        break

print('='*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('='*40)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()

while True:
    busca = int(input('Buscar o dado de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com código {busca}.')
    else:
        print(f'=== LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i,v in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {v} gols.')
        print('-'*30)
print('VOLTE SEMPRE')







tab = 0
cont = 1
while True:
    t1 = int(input('Digite um número para saber a sua tabuada [Negativo para parar]: '))
    if t1 < 0:
        break
    for c in range(1, 11):
        tab = t1 * c
        cont += 1
        print(f'{t1} x {c} = {tab}')



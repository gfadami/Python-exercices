lista = []
n_par = []
n_impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
for n in lista:
    if n % 2 == 0:
        n_par.append(n)
    if n % 2 == 1:
        n_impar.append(n)
print(f'Os números pares: {n_par}.')
print(f'Os números ímpares: {n_impar}.')




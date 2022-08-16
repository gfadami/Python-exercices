lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}.')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')


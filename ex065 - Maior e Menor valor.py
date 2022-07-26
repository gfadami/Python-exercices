resp = ['N']
cont = 0
soma = 0
maior = 0
menor = 0
while resp != 'N':
    n1 = int(input('Digite um valor: '))
    cont += 1
    soma += n1
    if cont == 1:
        menor = n1
        maior = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resp = input('Deseja continuar? [S/N]: ').strip().upper()
media = soma / cont
print(f'Você digitou {cont} números. A soma deles foi de {soma} e a média {media}. O maior número foi {maior} e o menor {menor}.')

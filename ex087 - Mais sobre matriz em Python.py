lista = list()
linha1 = list()
linha2 = list()
linha3 = list()
pares = list()
impares = list()
maior = menor = 0

for a in range(0,3):
    linha1.append(int(input(f'Digite o valor para [0,{a}]: ')))

for b in range(0,3):
    linha2.append(int(input(f'Digite o valor para [1,{b}]: ')))
    if b == 0:
        maior = menor = linha2[b]
    else:
        if linha2[b] > maior:
            maior = linha2[b]
        if linha2[b] < menor:
            menor = linha2[b]

for c in range(0,3):
    linha3.append(int(input(f'Digite o valor para [2,{c}]: ')))

lista.append(linha1[:])
lista.append(linha2[:])
lista.append(linha3[:])

for d in linha1:
    if d % 2 == 0:
        pares.append(d)
    if d % 2 == 1:
       impares.append(d)
for e in linha2:
    if e % 2 == 0:
        pares.append(e)
    if e % 2 == 1:
       impares.append(e)
for f in linha2:
    if f % 2 == 0:
        pares.append(f)
    if f % 2 == 1:
       impares.append(f)

print(f'[  {lista[0][0]}  ][  {lista[0][1]}  ][  {lista[0][2]}  ]')
print(f'[  {lista[1][0]}  ][  {lista[1][1]}  ][  {lista[1][2]}  ]')
print(f'[  {lista[2][0]}  ][  {lista[2][1]}  ][  {lista[2][2]}  ]')
print('='*30)
print(f'A soma de todas os valores pares digitados é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {lista[0][2]+lista[1][2]+lista[2][2]}.')
print(f'O maior valor da segunda linha é {maior}.')




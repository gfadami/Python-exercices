n1 = (int(input('Digite o primeiro valor: ')),
          int(input('Digite o segundo valor: ')),
          int(input('Digite o terceiro valor: ')),
      int(input('Digite o quarto valor: ')))
v1 = n1.count(9)
print(f'Você digitou os valores {n1}.')
print(f'O número 9 apareceu {v1} vezes.')
if 3 not in n1:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O valor 3 apareceu na {n1.index(3)+1}a posição.')
for n in n1:
    if n % 2 == 0:
        print(f'Os valores pares digitados foram {n}.')







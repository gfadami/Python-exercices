n1 = int(input('Digite um número (999 para parar): '))
cont = 1
soma = n1
while n1 != 999:
    n1 = int(input('Digite um número: '))
    if n1 != 999:
        cont +=1
        soma += n1
print(f'Você digitou {cont} vezes e a soma dos números foi {soma}.')

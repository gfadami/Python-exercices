c = s = 0
while True:
    n1 = int(input('Digite um número [999 para parar]: '))
    if n1 == 999:
        break
    c += 1
    s += n1
print(f'Você digitou {c} números e a soma entre eles foi de {s}.')

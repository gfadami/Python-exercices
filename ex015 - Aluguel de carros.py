n1 = int(input('Quantidade de dias alugados: '))
n2 = float(input('Quantidade de km percorrido: '))
n3 = (n1*60)+(n2*0.15)
print(f'{n1} dias alugados e {n3:.2f}km percorridos = R${n3:.2f}.')

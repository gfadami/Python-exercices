n1 = int(input('Digite o 1o número: '))
n2 = int(input('Digite o 1o número: '))
n3 = 0
while n3 != 5:
    n3 = int(input('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\nSua escolha: '))
    if n3 !=5:
        if n3 == 1:
            print(f'== A soma é {n1 + n2}. ==')
        elif n3 == 2:
            print(f'== A multiplicação é {n1 * n2}. ==')
        elif n3 == 3:
            if n1 > n2:
                print(f'== O maior número é {n1}. ==')
            elif n2 > n1:
                print(f'== O maior número é {n2}. ==')
            elif n1 == n2:
                print('== Os núemros são iguais. ==')
        elif n3 == 4:
            n1 = int(input('Digite o 1o número: '))
            n2 = int(input('Digite o 1o número: '))
print('FIM.')



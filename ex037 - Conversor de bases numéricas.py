n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite: \n [1] para BINÁRIO \n [2] para OCTAL \n [3] para HEXADECIMAL. \n Sua opção: '))
if n2 == 1:
    print(f'{n1} convertido para binário é {bin(n1)[2:]}.')
elif n2 == 2:
    print(f'{n1} convertido para octal é {oct(n1)[2:]}.')
elif n2 == 3:
    print(f'{n1} convertido para hexadecimal é {hex(n1)[2:]}.')
else:
    print('Opção inválida. Tente novamente.')



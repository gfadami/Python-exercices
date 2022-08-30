def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO. Digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário não digitou os dados.')
            return 0
        else:
            return n


def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO. Digite um número real válido.')
        except KeyboardInterrupt:
            print('O usuário não digitou os dados.')
            return 0
        else:
            return n


numInt = leiaInt('Digite um numero inteiro: ')
numReal = leiaReal('Digite um número real: ')
print(f'O número inteiro digitado foi {numInt} e o real foi {numReal}.')

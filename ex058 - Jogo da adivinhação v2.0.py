from random import randint
from time import sleep
cont = 1
e1 = randint(0,10)
e2 = int(input('Pensei em um número. Tente adivinhar: '))
print('PROCESSANDO...')
sleep(2)
while e2 != e1:
    print('Você errou, tente novamente.')
    e2 = int(input('Pensei em um número. Tente adivinhar: '))
    cont+=1
    if e1>e2:
        print('Mais...tente de novo.')
    elif e1<e2:
        print('Menos...tente de novo.')
print(f'Você acertou. Pensei no número {e1} e você precisou de {cont} tentativa(s) para acertar.')

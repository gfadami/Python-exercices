import random
from time import sleep
print('=== MEGA SENA ===')
palpites = int(input('Quantos jogos você quer?: '))
jogo = list()
for p in range(1, palpites+1):
    numeros = random.sample(range(1,60),6)
    jogo.append(numeros)
    sleep(1)
    print(f'Jogo {p}: {jogo[0]}.')
    jogo.clear()
print('=== BOA SORTE ===')
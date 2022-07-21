from random import choice
j1 = ['Pedra', 'Papel', 'Tesoura']
j5 = choice(j1)
c1 = str(input('Escolha Pedra, Papel ou Tesoura: ')).strip().capitalize()
if c1 == j5:
    print(f'Você escolheu {c1} e eu {j5}. EMPATE.')
elif c1 == 'Tesoura' and j5 == 'Papel':
    print(f'Você escolheu {c1} e eu {j5}. VOCE GANHOU.')
elif c1 == 'Papel' and j5 == 'Pedra':
    print(f'Você escolheu {c1} e eu {j5}. VOCE GANHOU.')
elif c1 == 'Pedra' and j5 == 'Tesoura':
    print(f'Você escolheu {c1} e eu {j5}. VOCE GANHOU.')
elif c1 == 'Tesoura' and j5 == 'Pedra':
    print(f'Você escolheu {c1} e eu {j5}. VOCE PERDEU.')
elif c1 == 'Papel' and j5 == 'Tesoura':
    print(f'Você escolheu {c1} e eu {j5}. VOCE PERDEU.')
elif c1 == 'Pedra' and j5 == 'Papel':
    print(f'Você escolheu {c1} e eu {j5}. VOCE PERDEU')
    
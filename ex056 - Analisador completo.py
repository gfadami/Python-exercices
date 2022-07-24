somaidade = 0
velho = 0
totmul20 = 0
n1 = ''
for p in range(1,5):
    print(f'{p}a PESSOA:')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        velho = idade
        n1 = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        n1 = nome
    if sexo in 'Ff' and idade < 20:
        totmul20 += 1
print(f'A média de idade é {somaidade/4:.2f}.')
print(f'O mais velho {n1} tem {velho} anos.')
print(f'{totmul20} mulheres tem menos de 20 anos.')







from random import randint
numeros = []
def sorteia():
    for c in range(0,5):
        numeros.append(randint(1,10))
    print(f'Os valores sorteados da lista: {numeros}.')


def somaPar():
    num = numeros[:]
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {num}, temos {soma}.')


sorteia()
somaPar()

from time import sleep
def maior(*num):
    cont = maior = 0
    for v in num:
        print(f'{v} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'\nForam informados {cont} valores, e o maior foi {maior}.')



maior(4,9,3)
maior(1,9,23,7,4,5)
maior(0)
maior(3,1,6,7)

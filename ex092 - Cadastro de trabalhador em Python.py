from datetime import date
trab = dict()
lista = []
while True:
    trab['nome'] = str(input('Seu nome: '))
    trab['idade'] = date.today().year - (int(input('Ano de nascimento: ')))
    trab['ctps'] = int(input('Carteira de trabalho [0 não tem]: '))
    if trab['ctps'] == 0:
        lista.append(trab.copy())
        break
    trab['contratação'] = int(input('Ano de contratação: '))
    trab['salario'] = float(input('Salário: '))
    trab['aposentadoriaano'] = (trab["contratação"]) + 35
    trab['aposentadoriaidade'] = (trab["idade"]) + 35
    lista.append(trab.copy())
    print(trab)
    break
for k, v in trab.items():
    print(f'O campo {k} tem valor {v}.')
    



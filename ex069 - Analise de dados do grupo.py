print('== CADASTRE UMA PESSOA ==')
soma = contid = contsex = femenor = 0
while True:
    idade = input('Digite a idade: ')
    while not idade.isdigit():              ## Quando a idade for um input, ele vai armazenar na linha 7 como input. Se for um str ele pergunta de novo.
        idade = input('Digite a idade: ')
    idade = int(idade)
    sexo = str(input('Digite o sexo: ')).strip().upper()
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo: ')).strip().upper()
    exit = str(input('Quer continuar [S/N]?: ')).strip().upper()
    if sexo == 'F' and idade <= 20:
        femenor += 1
    if idade >= 18:
        contid += 1
    if sexo == 'M':
        contsex += 1
    if exit == 'N':
        break

print(f'Ao total {contid} tem mais de 18 anos, {contsex} do sexo masculino e {femenor} mulhere(s) menore(s) de 20 anos.')

p1 = float(input('Qual o seu peso?: '))
a1 = float(input('Qual a sua altura?: '))
imc = p1 / (a1**2)
print(f'O IMC é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Peso ideal.')
elif 25 <= imc <= 30:
    print('Acima do peso.')
elif 30 <= imc <= 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade morbida.')
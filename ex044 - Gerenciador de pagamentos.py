p1 = float(input('Qual o preço da compra? R$: '))
print('''FORMAS DE PAGAMENTO
[1] A VISTA NO DINHEIRO
[2] A VISTA NO CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO
''')
op = int(input('Qual a sua opção?: '))
if op == 1:
    t1 = p1 - (p1*10/100)
elif op == 2:
    t1 = p1 - (p1*5/100)
elif op == 3:
    t1 = p1
    parcela = t1/2
    print(f'Sua compra será parcelada em 2x de {parcela}. SEM JUROS')
elif op == 4:
    t1 = p1 + (p1*20/100)
    totalparc = int(input('Quantas parcelas?: '))
    parcela = t1 / totalparc
    print(f'Sua compra será parcela em {totalparc}x de R$ {parcela}. COM JUROS ')
else:
    t1 = p1
    print('Comando inválido. Tente novamente.')
print(f'Sua compra de {p1:.2f} vai custar {t1:.2f}.')





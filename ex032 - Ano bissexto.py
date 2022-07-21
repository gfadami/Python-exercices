from datetime import date
a1 = int(input('Em que ano estamos? Para o ano atual coloque o valor zero: '))
if a1 == 0:
    a1 = date.today().year
if (a1%4==0 and a1%100!=0) or (a1%400==0):
    print(f'O ano {a1} é bissexto.')
else:
    print(f'O ano {a1} não é bissexto.')

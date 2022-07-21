r1 = float(input('Write the first number: '))
r2 = float(input('Write the second number: '))
r3 = float(input('Write the third number: '))
if (r1+r2 > r3) and (r2+r3 > r1) and (r1+r3 > r2):
    print('It is a triangle.')
    if r1==r2==r3:
        print('EQUILATERAL')
    elif r1!=r2!=r3!=r1:
        print('SCALENO')
    else:
        print('ISOSCELES')

else:
    print('Is not a triangle.')

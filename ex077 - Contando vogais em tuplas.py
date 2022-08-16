lista = ('aprender', 'programr', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'mercado', 'programador', 'futuro')
for p in lista:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')

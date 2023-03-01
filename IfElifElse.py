a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
if a > b and a > c:
    print('O maior numero é {}'.format(a))
elif b > a and b > c:
    print('O maior numero é {}'.format(b))
elif c > a and c > b:
    print('O maior numero é {}'.format(c))
if a == b and a != c:
    print(f'O primeiro e segundo valores são iguais, {a}')
elif a == c and a != b:
    print(f'O primeiro e o terceiro valores são iguais, {a}')
elif a == c and a == b:
    print(f'Todos os valores são iguais, {a}')
else:
    print(f'Todos os valores são diferentes,1°={a}, 2°={b} e 3°={c}')

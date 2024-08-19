print('=' * 30)
print('DIGITE 3 VALORES DIFERENTES')
print('=' * 30)
n1 = int(input('\033[1;31;mDigite um número:\033[m'))
n2 = int(input('\033[1;31;mDigite um número:\033[m'))
n3 = int(input('\033[1;31;mDigite um número:\033[m'))
cores = {'limpa': '\033[m', 'vermelho': '\033[31;m'}

if n1 == n2 == n3:
    print('TODOS os valores tem que ser DIFERENTES')
if n1 == n2:
    print('TODOS os valores tem que ser DIFERENTES')
if n2 == n3:
    print('TODOS os valores tem que ser DIFERENTES')
if n1 == n3:
    print('TODOS os valores tem que ser DIFERENTES')

if (n1 + n2) > (n2 + n3) and (n1 + n3) > (n2 + n3):
    print(f'O maior é número {n1}')
    if (n1 + n2) > (n1 + n3):
        print(f'O menor número é {n3}')
    if (n1 + n3) > (n1 + n2):
        print(f'O menor número é {n2}')


if (n2 + n1) > (n1 + n3) and (n2 + n3) > (n1 + n3):
    print(f'O maior é número {n2}')
    if (n1 + n2) > (n2 + n3):
        print(f'O menor número é {n3}')
    if (n2 + n3) > (n1 + n2):
        print('O menor número é {}'.format(n1))


if (n3 + n1) > (n1 + n2) and (n3 + n2) > (n1 + n2):
    print(f'O maior é número {n3}')
    if (n3 + n2) > (n3 + n1):
        print(f'O menor número é {n1}')
    if (n3 + n1) > (n3 + n2):
        print(f'O menor número é {n2}')



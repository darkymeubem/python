n1 = int(input('\033[1;36mDigite um número: '))
n2 = int (input('\033[1;36mDigite um número: '))
lista = [1,2,3,4,5]
d = input('Digite: \n\033[1;33m[1]\033[m \033[1;34msomar\033[m\n\033[1;33m[2]\033[m \033[1;34mmultiplicar\033[m\n\033[1;33m[3]\033[m \033[1;34mpara saber qual dos números é maior\033[m\n\033[1;33m[4]\033[m \033[1;34mnovos números\033[m\n\033[1;33m[5]\033[m \033[1;34mpara sair do programa\033[m\n')
if d == '1':
    print(f'A soma dos números \033[1;31m{n1}\033[m e \033[1;31m{n2} é igual a \033[1;34m{n1 + n2} ')
if d == '2':
    print(f'A multiplicação dos números \033[1;31m{n1}\033[m e \033[1;31m{n2}\033[m é igual a \033[1;34m{n1 * n2} ')
if d == '3':
    if n1 > n2:
        print(f'\033[1;35m{n1}\033[m é \033[1;31mmaior')
    else:
        print(f'\033[1;35m{n2}\033[m é \033[1;31mmaior.')
while d == '4':
    n3 = int(input('\033[1;36mDigite um número: '))
    n4 = int(input('\033[1;36mDigite um número: '))
    d = input('Digite: \n\033[1;33m[1]\033[m \033[1;34msomar\033[m\n\033[1;33m[2]\033[m \033[1;34mmultiplicar\033[m\n\033[1;33m[3]\033[m \033[1;34mpara saber qual dos números é maior\033[m\n\033[1;33m[4]\033[m \033[1;34mnovos números\033[m\n\033[1;33m[5]\033[m \033[1;34mpara sair do programa\033[m\n')
    if d == '1':
        print(f'A soma dos números \033[1;31m{n3}\033[m e \033[1;31m{n4}\033[m é igual a \033[1;34m{n3 + n4} ')
    if d == '2':
        print(f'A multiplicação dos números \033[1;31m{n3}\033[m e \033[1;31m{n4}\033[m é igual a \033[1;34m{n3 * n4} ')
    if d == '3':
        if n3 > n4:
            print(f'\033[1;35m{n3}\033[m é \033[1;31mmaior')
        else:
            print(f'\033[1;35m{n4}\033[m é \033[1;31mmaior.')
    if d == 5:
        print('\033[1;31mVocê saiu do programa.')
if d == '5':
    print('\033[1;31mVocê saiu do programa.')
    
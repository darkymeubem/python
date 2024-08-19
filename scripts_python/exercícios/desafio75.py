n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tupla = (n1,n2,n3,n4)


print(f'Foram {tupla.count(9)} vezes que o 9 foi digitado')

if tupla[0] == 3:
    print('O primeiro 3 apareceu na posição 1')
if tupla[0] != '3':
    if tupla[1] == 3:
        print('O primeiro 3 apareceu na posição 2')
if tupla[0] != 3:
    if tupla[1] != 3:
        if tupla[2] == 3:
            print('O primeiro 3 apareceu na posição 3')
if tupla[0] != 3:
    if tupla[1] != 3:
        if tupla[2] != 3:
            if tupla[3] == 3:
                print('O primeiro 3 apareceu na posição 4')
print('Os valores par digitados são:',end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n,end=' ')
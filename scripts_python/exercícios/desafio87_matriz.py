num = [[[],[],[]],[[],[],[]],[[],[],[]]]
soma = 0
coluna_3 = []
valores = 0
s_c3 = 0
for c in range(0,3):
    if c == 0:
        for d in range(0,3):
            valores = int(input(f'\033[1mDigite um número para a posição\033[m \033[1;31m(\033[m\033[1;34m{c+1}\033[m\033[1m,\033[m \033[1;34m{d+1}\033[m\033[1;31m)\033[m\033[1m:\033[m '))
            num[c][d].append(valores)
            if d == 2:
                coluna_3.append(valores)
            if valores % 2 == 0:
                soma = valores + soma


    elif c == 1:
        for d in range(0,3):
            valores = int(input(f'\033[1mDigite um número para a posição\033[m \033[1;31m(\033[m\033[1;34m{c+1}\033[m\033[1m,\033[m \033[1;34m{d+1}\033[m\033[1;31m)\033[m\033[1m:\033[m '))
            num[c][d].append(valores)
            if d == 2:
                coluna_3.append(valores)
            if valores % 2 == 0:
                soma = valores + soma

    else:
        for d in range(0,3):
            valores = int(input(f'\033[1mDigite um número para a posição\033[m \033[1;31m(\033[m\033[1;34m{c+1}\033[m\033[1m,\033[m \033[1;34m{d+1}\033[m\033[1;31m)\033[m\033[1m:\033[m '))
            num[c][d].append(valores)
            if d == 2:
                coluna_3.append(valores)
            if valores % 2 == 0:
                soma = valores + soma
for a in range(0,len(coluna_3)):
    s_c3 = coluna_3[a] + s_c3

print('\033[34m=\033[m\033[35m-\033[m' * 25)
for c in range(0,len(num)):
    for d in range(0,len(num)):
        print(num[c][d], end= ' ')
    print('\n')
print('\033[34m=\033[m\033[35m-\033[m' * 25)
print(f'\033[1mA soma de todos os valores par é\033[m \033[1;34m{soma}\033[m\n\033[1mA soma dos valores digitados na coluna 3 é\033[m \033[1;34m{s_c3}\033[m\n\033[1mO maior número da coluna 2 é\033[m \033[1;34m{str(max(num[1])).replace("[","").replace("]","")}')

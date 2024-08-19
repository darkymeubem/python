num = [[[],[],[]],[[],[],[]],[[],[],[]],]
for c in range(0,3):
    if c == 0:
        for d in range(0,3):
            num[c][d].append(int(input(f'Digite um número para a posição ({c}, {d}): ')))
    elif c == 1:
        for d in range(0,3):
            num[c][d].append(int(input(f'Digite um número para a posição ({c}, {d}): ')))
    else:
        for d in range(0,3):
            num[c][d].append(int(input(f'Digite um número para a posição ({c}, {d}): ')))
print('=-_' * 20)
for c in range(0,len(num)):
    for d in range(0,len(num)):
        print(num[c][d], end= ' ')
    print('\n')
print('=-_'*20)

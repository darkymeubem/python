n = []
n.append(int(input('Digite primeiro numero: ')))
n.append(int(input('Digite segundo numero: ')))
n.append(int(input('Digite terceiro numero: ')))
n.sort()
print('O menor numero é {}.'.format(n[0]))
print('O maior numero é {}.'.format(n[2]))
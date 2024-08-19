a1 = int(input('Informe o valor do a1: '))
r = int(input('Qual o valor da razão? '))
c = 0
while c != 10:
    c = c + 1
    print(f'a{c} = {a1 + (c*r) - r}')

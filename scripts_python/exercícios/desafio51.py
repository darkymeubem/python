a1 = int(input('Informe o valor do a1: '))
r = int(input('Qual o valor da razão? '))
print(f'a1 = {a1} ')
for c in range (2,11):
    print(f'a{c} = {a1 + (c*r) - r}')
lista = []
par = []
imp = []
resp = ''
p = 0
i = 0
while resp != 'N':
    valores = int(input('Digite um número: '))
    resp = input('Você quer continuar? [S/N] ').upper().strip()
    lista.append(valores)
    if valores % 2 == 0:
        par.append(valores)
        p = p + 1
    if valores % 2 == 1:
        imp.append(valores)
        i = i + 1
print('='*57)
print(f'Você digitou os valores {lista}, sendo eles:')
print(f'{p} pares, {par}')
print(f'{i} ímpares, {imp}')
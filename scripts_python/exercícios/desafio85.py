n = [[],[]]
valores = 0
for c in range(0,7):
    valores = int(input('Digite um número: '))
    if valores % 2 == 0:
        n[0].append(valores)
    else:
        n[1].append(valores)
n[0].sort()
n[1].sort()
print(f'Os valores par são: {n[0]}\nOs valores ímpares são: {n[1]}')

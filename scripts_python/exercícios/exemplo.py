def dobra(lst):
    for c in range(0,5):
        print(lst[c] * 2)


valores = []

for c in range(0,5):
    valores.append(int(input('Digite um número: ')))
print(valores)
dobra(valores)
lista = []

for c in range (0,5):
    valores = int(input('Digite um número: '))
    if c == 0 or valores > lista[-1]:
        lista.append(valores)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if valores <= lista[pos]:
                print(f'Valor adicionado na posição {pos}')
                lista.insert(pos,valores)
                break
            pos = pos + 1
print(lista)
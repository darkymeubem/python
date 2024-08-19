lista = []
s = 0
c = 0

maior = []
menor = []
a = []
for c in range (0,5):
    lista.append(int(input('Digite um valor: ')))
for pos,d in enumerate(lista):
    if d == max(lista):
        maior.append(pos+1)
    if d == min(lista):
        menor.append(pos+1)


print('Você digitou os valores',end=' ')
for e in range (0,5):
    print(lista[e],end=' ')
print('\n')
print('=-_' * 20)
print(f'O maior valor é {max(lista)} e sua posição é {str(maior)}'.replace("[","").replace("]","").replace(","," e"))
print(f'O menor valor é {min(lista)} e sua posição é {str(menor)}'.replace("[","").replace("]","").replace(","," e"))
print('=-_' * 20)

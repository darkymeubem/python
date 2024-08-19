import random
lista = []
for c in range(0,6):
    lista.append(random.randint(0,60))
print('=-'*30)
print(f'Os valores sorteados foram: {lista}')
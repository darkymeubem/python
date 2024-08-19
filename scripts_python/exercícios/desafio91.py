from random import randint
from time import sleep
dados = {'jogador1': randint(1,6),'jogador2': randint(1,6),'jogador3': randint(1,6),'jogador4': randint(1,6)}
lista = [dados["jogador1"],dados["jogador2"],dados["jogador3"],dados["jogador4"]]
a = 0
ranking = []
pos = []
for k,v in dados.items():
    print(f'\033[1mO\033[m \033[1;34m{k}\033[m \033[1mtirou\033[m \033[1;31m{v}\033[m')
    sleep(0.5)
    lista.sort(reverse= True)
jogar = ''
for p in range(0,4):
    sleep(0.5)
    print(f'\033[1m{p+1}° lugar:\033[m',end=' ')
    for k,v in dados.items():
        if v == lista[p] and jogar != k:
            sleep(0.5)
            print(f'\033[1;34m{k}\033[m \033[1mcom\033[m \033[1;31m{v}\033[m')
            jogar = k
            break


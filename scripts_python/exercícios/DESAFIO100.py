from random import randint
from time import sleep
lista = []
spar = 0
for c in range(0,5):
    lista.append(randint(0,100))
    if lista[c] % 2 == 0:
        spar = lista[c] + spar

def sorteia(valor):
    print(f'Sorteando {len(valor)} valores: ',end='')
    for a in range(0,len(valor)):
        sleep(.3)
        print(valor[a], end=' ')
def somapar(valores):
    print(f'\nA soma dos valores par é igual a {valores}')
sorteia(lista)
somapar(spar)




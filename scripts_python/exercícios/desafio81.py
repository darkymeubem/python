lista = []
resposta = ''
c = 0
v = 0
pos5 = []
while resposta != 'N':
    c = c + 1
    valores = int(input('Digite um número: '))
    lista.append(valores)
    resposta = input('Você quer continuar? [S/N] ').upper().strip()
    if valores == 5:
        pos5.append(c)

    lista.sort(reverse=True)
print('=-_'*20)
print(f'Foram {c} valores digitados\nA lista em ordem decrescente é {lista}')
if 5 in lista:
    for d in range(0,len(pos5)):
        print(f'5 foi digitado na posição: {pos5[d]}')
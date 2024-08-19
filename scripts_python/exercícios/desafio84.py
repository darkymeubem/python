




lista = []
rapaziada = []
l = []
resposta = ''
p = []
c = 0
maiorp = 0
menorp =0
while resposta != 'N':
    c = c + 1
    lista.append(str(input('Nome: ')).capitalize().strip())
    lista.append(int(input('Peso: ')))
    resposta = str(input('Você quer continuar? [S/N] ')).upper().strip()
    rapaziada.append(lista[:])
    lista.clear()
for x in rapaziada:
    if x[1] >= 90:
        p.append(x[0])

    else:
        l.append(x[0])

print('=-'*30)
print(f'Ao todo foram cadastradas {c} pessoas')
print(f'O maior peso foi {max(rapaziada)[1]}Kg.As pessoas "pesadas" são: {p}')
print(f'O menor peso foi {min(rapaziada)[1]}Kg.As pessoas "leves" são: {l}')

lista = []
geral = []
resp = ''
media = []
m = -1
numb = 0
while resp != 'N':
    lista.append(str(input('Informe seu nome: ')).strip().capitalize())
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    resp = str(input('Você quer continuar? [S/N]')).strip().upper()
    geral.append(lista[:])
    lista.clear()
for c in range(0,len(geral)):
    m = (geral[c][1] + geral[c][2]) / 2
    media.append(m)
print('=-' * 20)
print('{}{}{}{}{}'.format('No.',' ' * 3 ,'Nome',' '*11,'Média'))
print('=' * 28)
for a in range(0,len(geral)):
    print('{}{}{}{}{:.1f}'.format(a,' '*5,geral[a][0],' ' * (15 - len(geral[a][0])),media[a]))


while numb != 999:
    numb = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('=' * 50)
    print('\n')
    if numb != 999:
        print(f'Notas de {geral[numb][0]} são: {geral[numb][1], geral[numb][2]}')
print('\033[1m{:^50}'.format('Programa Finalizado'))
print('')
print('')
print('=' * 50)
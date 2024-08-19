
def ficha(nome, gols):
    if nome == '':
        nome = 'desconhecido'
    if gols == '':
        gols = '0'

    print(f'O {nome} fez {gols} gols.')

ficha(str(input('Nome do jogador: ')),
    str(input('Número de gols: ')))

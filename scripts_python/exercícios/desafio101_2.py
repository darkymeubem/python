def voto(ano = 0):
    i = 2021 - ano
    if i >= 18 and i < 65:
        print(f'Com {i} anos: o voto é OBRIGATÓRIO')

    elif i >= 16 and i < 18 or i >= 65 and i < 120:
        print(f'Com {i} anos: o voto é OPCIONAL')

    elif i >= 120:
        print('Digite uma idade válida! ')



    else:
        print(f'Com {i} anos: o voto NÃO É OBRIGATÓRIO')

num = int(input('Digite seu ano de nascimento: '))
voto(num)
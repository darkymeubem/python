def voto(idade):
    i = 2020 - idade
    if i < 18 and i != 16 and i != 17:
        print(f'Você  tem {i} anos e não é obrigado a votar ainda')
    elif i > 18 and i < 65:
        print(f'Caro votante, você tem {i} anos e é obrigado a votar.')
    else:
        print('Você vota se quiser :/')
voto(int(input('Ano de Nascimento: ')))
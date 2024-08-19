from ex111.utilidadesCeV import dados


def resumo(a = 0, b=0, c=0):


    d = str(a)
    e = str(b)
    f = str(c)
    tam = len(f'{10 * " ":<}RESUMO DO VALOR{10 * " ":>}')
    print(tam * "=")
    print(f'{10 * " ":<}RESUMO DO VALOR{10 * " ":>}')
    print(tam * "=")
    print(f'Preço analisado:{(tam - len("preço analisado:") - len(d) - 5) * " "}{dados.moeda(a)}')
    print(f'Dobro do preço:{(tam - len("dobro do preço:") - len(d) - 5) * " "}{dados.dobro(a, True)}')
    print(f'Metade do preço:{(tam - len("metade do preço:") - len(d) - 5) * " "}{dados.metade(a, True)}')
    print(f'{b}% de aumento:{(tam - len(f"{e}% de aumento:") - len(d) - 5) * " "}{dados.aumenta(a, b, True)}')
    print(f'{c}% de redução:{(tam - len(f"{f}% de aumento:") - len(d) - 5) * " "}{dados.reduz(a, c, True)}')
    print('=' * tam)
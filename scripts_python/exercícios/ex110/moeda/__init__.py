from ex109 import moeda

def resumo(a = 0, b = 0, c =0):
    g = 'Resumo do valor'
    d = str(a)
    e = str(b)
    f = str(c)
    tam = len(f'{10 * " ":<}RESUMO DO VALOR{10 * " ":>}')
    print(tam*"=")
    print(f'{10 * " ":<}RESUMO DO VALOR{10 * " ":>}')
    print(tam*"=")
    print(f'Preço analisado:{(tam - len("preço analisado:") - len(d) - 5) * " "}{moeda.moeda(a)}')
    print(f'Dobro do preço:{(tam - len("dobro do preço:") - len(d) - 5) * " "}{moeda.dobro(a,True)}')
    print(f'Metade do preço:{(tam - len("metade do preço:") - len(d) - 5) * " "}{moeda.metade(a,True)}')
    print(f'{b}% de aumento:{(tam - len(f"{e}% de aumento:") - len(d) - 5) * " "}{moeda.aumenta(a, b,True)}')
    print(f'{c}% de redução:{(tam - len(f"{f}% de aumento:") - len(d) - 5) * " "}{moeda.reduz(a,c, True)}')
    print('=' * tam)
    
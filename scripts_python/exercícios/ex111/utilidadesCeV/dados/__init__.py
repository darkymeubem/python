def metade(a =0, df = False):
    a = a / 2
    if df == True:
        return f'R${a:.2f}'.replace('.', ',')

    return a

def dobro(b = 0,df = False):
    b = b*2
    if df == True:
        return f'R${b:.2f}'.replace('.', ',')
    return b

def aumenta(c = 0,taxa = 0,df = False):
    c = float(c + c * taxa/100)
    if df == True:
        return f'R${c:.2f}'.replace('.', ',')
    return c

def reduz(d = 0,taxa = 0, df = False):
    d =float(d - d * taxa/100)
    if df == True:
        return f'R${d:.2f}'.replace('.', ',')
    return d

def moeda(preco = 0,moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')





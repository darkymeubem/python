from ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p):.0f}')
print(f'O dobro de {p} é {moeda.dobro(p):.0f}')
print(f'Aumentando 10%, temos {moeda.aumenta(p,10):.2f} ')
print(f'Reduzindo 10%, temos {moeda.reduz(p,10):.2f}')